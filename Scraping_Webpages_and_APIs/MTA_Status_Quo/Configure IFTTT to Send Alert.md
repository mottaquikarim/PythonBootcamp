# Configure IFTTT to Send Alert

Our final step for this app is to send meaningful alerts to an external source - email, text, etc - letting us know that the trains r fucked.

There are many ways to achieve this, but we will specifically look into integrating with the [IFTTT Maker Webhook API](https://ifttt.com/maker_webhooks) which lets **us** make a call to IFTTT whenever we feel like it.

IFTTT, short for [If This Then That](https://ifttt.com/), is a service that allows users to chain together triggers and actions without having to write any code. The Maker Webhook can act as a trigger which we can then use to send ourselves a text or email.

## Set up code to trigger IFTTT

Take the `filter_by_lines` function and call it for the subway line(s) you use most often / will need to get home tonight. Then:

1. Determine if any of the lines you filtered by are delayed.
2. If any of the lines you care about **are** delayed, trigger a **POST** request to the IFTTT Maker Webhook endpoint with the names of the lines that are delayed.
3. Configure IFTTT to send a text or email if trigger is received.
4. Test your code and ensure that it works!

(Note, I purposefully skimped on documentation here - it's important to be able to sniff out the correct docs for tasks on your own as you mature in your programming background! Goodluck!)

## BACKGROUND: Drawbacks

The main drawback to this technique is that if your computer is turned off or PyCharm is closed...nothing happens. 

To circumvent this, we can upload our code to **pythonanywhere**, which will run our code on the cloud. Look through pythonanywhere docs to see if there is an easy way to upload a PyCharm project to it. You can also set up your code in pythonanywhere to run every hour or every 30 mins via something called a **CRON** job which means you can get more "real-time" notifications of subway slowdowns. 
