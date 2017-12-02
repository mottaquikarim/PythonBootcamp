# Scraping Webpages and APIs

Here we will apply what we have learned about the basics of python to do more useful things in terms of data accumulation. Specifically, we will look into how we can harvest data that might be useful for processing from online sources: webpages and publicly available APIs.


## Rules of Engagement
For all exercises, partner with someone next to you. Coding is **collaborating**. Talk through each problem and attempt to arrive at the solution **together**. Remember, it's ok to break stuff and get things wrong, that's the **only** way to learn!


## THEME: Automating Life

🎉🎈🎂🍾🎊🍻💃

We are superpowered pythonic humans! Let's use our powers for good/evil! In this unit, we will look at how we can make our lives easier by gathering data freely available on websites in a structured and repeatable manner.

### [MTA Status Quo](MTA_Status_Quo/README.md)

🚇 ✋ 🛑 🖕🖕 

Or, which lines are fucked today?

#### [1. GET MTA Homepage Programmatically](MTA_Status_Quo/GET%20MTA%20Homepage%20Programmatically.md)
#### [2. Parse HTML and Search](MTA_Status_Quo/Parse%20HTML%20and%20Search.md)
#### [3. Isolate Subway Status Data](MTA_Status_Quo/Isolate%20Subway%20Status%20Data.md)
#### [4. Tfrom Status Data to Dict](MTA_Status_Quo/Tfrom%20Status%20Data%20to%20Dict.md)
#### [5. Filter Status by Line](MTA_Status_Quo/Filter%20Status%20by%20Line.md)
#### [6. Configure IFTTT to Send Alert](MTA_Status_Quo/Configure%20IFTTT%20to%20Send%20Alert.md)

### How To Dress?

👗 👘 💃

Using the **[OpenWeatherMap API](https://openweathermap.org/api)**, check weather conditions in your area every morning and suggest articles of clothing / accessories that may be relevant. IE: if there is rain scheduled in the evening, suggest bringing an umbrella. Etc.


### Cards Against Humanity

🗂️ 🃏 ♥️ ♠️ ♦️ 🗂️

Did you know Cards Against Humanity is technically open source? Scrape [this github repo](https://github.com/nodanaonlyzuul/against-humanity) to grab all question and answer cards. Write a chatbot using the [Twilio API](https://www.twilio.com/) that will serve the user a random question card and a few randomly chosen answer cards. The user can text the bot back answer choices which the bot will then use to assemble the final string and send back.

### Watch Price on Amazon 

🏪 🛒 🛍️

Write a script that will watch a product on amazon, record the price and send alert if price decreases. To properly do this, look into using SQLite or `TinyDB` (python module) to store the previous price of the product. To make this really interesting, allow users to track price fluctuations of multiple products and also store average trends (ie: trend lines and other pretty graphs that show price changes)

### NYTimes Front Page Tracker

📰 🗞️ 📰

Query NYTimes Front Page on a daily basis and search all articles for references to a company or person of interest. If more than a certain threshold found, send alert. This one is interesting because it involves loading one page - finding all the anchors on that page - and then loading **all** of those anchors as well. Loops on loops on loops, yo.


## 🚗 Parking Lot

Just some interesting/useful links I found while prepping for this class...
