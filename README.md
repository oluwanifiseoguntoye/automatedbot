# Automated Email Shift Pick ups using Selenium & Gmail API
I made an automated bot that watches over my work email and picks up shifts for me depending on if it fits my availability

## A bit of background

<p>
  I am a computer science and Mathematics tutor for:
</p>

<img src="https://i.imgur.com/x1I5lVw.png" width="2000">

<p>
  Since the 2023 New Year, there's been a shift shortage where even if I submit up to 40 hours of availability in a week,
  I'd get the bare minimum, 4 hours. This has been going on all year and really impacted me as this is my sole income as a Student in Toronto. Until
  September, when I decided I was going to do something about it.
</p>

## Email Transfers

<p>
  Scheduled shifts <strong>aren't</strong> the only way to get hours in the week. We also have Shift Transfer Requests that come as emails which look like
</p>

<div align="center">
  <img src="https://i.imgur.com/4gLvnGu.png" width="500">
</div>

<p>
  These are scheduled shifts other tutors don't want so they request to have them transferred. Usually, these transfer requests disappear within the minute so I could never really get too many of them because they come at random times and they were too many steps involved which slowed down the pace I'd be picking up shifts—it was way too stressful. So I decided to make a bot that would do all of that for me.
</p>

## Results
<p>
  I made this bot back in September when school started because I couldn't afford to 1) Not get any shits and 2) Spend too much time watching my email. The automated bot is constantly running on my laptop needing no manual intervention to pick up shifts. It's been largely successful and I managed to pick up all the shift transfers that fit my availability— going from 4 hours to 20-30 weekly.
</p>

## Where to from here?
<p>
  This is my first python only project which is nice but I do feel like it's missing some things. I'd like to impliment a UI using <strong>React</strong> and <strong>Node</strong> soon for Backend and Frontend functions. I think this would make it more accessible to me. For instance, I'm using a Dictionary of Lists to mark my availability 
  currently. It would be cool to see if I could add functionality similar to when2meet.com where you just drag your availability. I could also add buttons to start the bot or set a time interval that it should always be turned on by etc etc. I feel I could do a lot here which is exciting. It was also really cool to build something that I use everyday.
</p>
