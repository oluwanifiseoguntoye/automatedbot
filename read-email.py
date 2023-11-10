from simplegmail import Gmail
from availability import availability_schedule
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

gmail = Gmail()

duration = 12 * 60 * 60
start_time = time.time()

chrome_options = ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--user-data-dir=/Users/nifiseoguntoye/Library/Application Support/Google/Chrome/")
chrome_options.add_argument('--profile-directory=Profile 7')

try:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    print("ChromeDriver is successfully initiated.")
except Exception as e:
    print(f"Error: {e}")

while time.time() - start_time < duration:  
    remaining_time = duration - (time.time() - start_time)

    shifts = {}
    messages = gmail.get_unread_inbox()

    for message in messages:
    
        if message.subject == "Shift Transfer Request":

            soup = BeautifulSoup(message.html, "html.parser")
            strong_tags = soup.find_all('strong')
            time_pattern = re.compile(r'\b\d{1,2}:\d{2} [APMapm]{2}\b')

            for strong_tag in strong_tags:
                time_match = time_pattern.search(strong_tag.text)
                weekday_match = re.search(r'\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b', strong_tag.text)

                if time_match:
                    extracted_time = str(time_match.group())

                if weekday_match:
                    extracted_weekday = str(weekday_match.group())

                    if extracted_weekday in availability_schedule:
                        if extracted_time in availability_schedule[extracted_weekday]:
                            date_key = str(message.date)
                            shifts[date_key] = {}
                            shifts[date_key][extracted_weekday] = extracted_time
                            print(f"Shift is available for {extracted_weekday} at {extracted_time}")

                            link = soup.find('a', class_=lambda x: x and 'mcnButton' in x)['href']
                            driver.get(link)

                            try:
                                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Sign in with email or SSO instead"]]')))
                                driver.find_element("xpath", '//button[.//span[text()="Sign in with email or SSO instead"]]').click()

                                try:
                                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Continue with Google"]]')))
                                    driver.find_element("xpath", '//button[.//span[text()="Continue with Google"]]').click()
                                    
                                    email_input = driver.find_element(By.ID, "identifierId").send_keys(username)
                                    driver.find_element(By.ID, "identifierNext").click()
                                    time.sleep(5)
                                    password_input = driver.find_element(By.NAME, "Passwd").send_keys(password)
                                    driver.find_element(By.ID, "passwordNext").click()
                                    time.sleep(20)

                                except Exception as e:
                                    print("Failed to click on Google", str(e))

                            except Exception as e:
                                print("Failed to click on SSO", str(e))
                            
                            message.mark_as_read()
                            screen_text = driver.find_element(By.ID, "modal-header-title").text

                            if "Shift Transfer was already picked up" in screen_text:
                                print("Too Slow, ", screen_text)
                            
                            else: 
                                print("Shift was accepted!")

        else: 
            message.mark_as_read()

    time.sleep(1)

driver.quit()