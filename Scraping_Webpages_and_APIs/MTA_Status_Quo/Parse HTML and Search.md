# Parse HTML and Search

Now that we have HTML data, let's figure out how to parse this data and search for information that may be useful to us.

## BACKGROUND: Searching and Querying HTML

The raw HTML that we get from the **requests** module is useful because it is the same exact HTML code that the browser gets and processes.

In order to extract useful information from this code, we can rely on techniques widely used by web programmers: DOM parsing and CSS selectors.

Essentially, HTML is an encoded representation of a data structure called a **tree** (you can construct a very primitive version of this structure in python today, actually - just nest a bunch of dicts within one another). 

The **tree** that is represented by HTML is called the **DOM**, or **Document Object Model** and CSS allows us to search and extract certain **nodes** (basically, HTML tags) of this tree with a simple but powerful querying language.

As it turns out, python provides a library that will turn the HTML code we get from our **requests** function call into a **tree** structure similar to the **DOM** that is constructed by the browser. Essentially we are able to mimic the web browser's functionality in python. We use the **[beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** library to achieve this.

## Using Beautiful Soup to Query HTML

First, you will want to install the **beautifulsoup** dependency through PyCharm. Remember to:

1. Install version 4+ of the software (last I checked PyCharm returned an older v3 as well)
2. Update `requirements.txt` with the library name and version number as shown in the previous section.

Continuing on from the code you wrote in the previous section, take the output of your GET request (the HTML string) and integrate it with beautiful soup so that the HTML is queryable. (Examples are in **[bs4 docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**).

Specifically, try to isolate the HTML tags that wrap the MTA website's **Service Status** section. Can you locate the current status of the subway systems?

(Image below to help you locate service status)

![mta](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/MTA_Service_Status.png?raw=true)

## ✋✋ ...Cavaeat
**DO NOT READ UNTIL YOU'VE ATTEMPTED THE PREVIOUS SECTION!!**

You should have noticed something very peculiar with the HTML code returned from the MTA page: the data for *most* of the site is returned, but the service statuses specifically **do not**!!

What gives?

Well, as it turns out, the MTA webpage uses **AJAX**, or Asynchronous JavaScript and XML to load the currently subway status (and probably keep it fresh in realtime). The main caveat for web scraping -- and this is important -- is that javascript is generalyl **not** well supported when fetching page data. (For javascript support, consider building your own browser! ...or other techniques beyond the scope of this workshop).

However, there is a way around this.

### 1. Open up your browser to the MTA.info page
![1](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/MTA_step1.png?raw=true)
### 2. Open Web Developer Tools
![2](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/MTA_step2.png?raw=true)
### 3. Open the `Network` Tab
![3](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/MTA_step3.png?raw=true)
### 4. Click the `XHR` subtab
![4](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/MTA_step4.png?raw=true)
### 5. Refresh the page and click into the first entry.
![5](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/MTA_step5.png?raw=true)

## Use `requests` to fetch the URL from XHR tab

Using the `requests` module, make a GET call to the URL from the XHR tab. If you explore that pane, you will see that it does not return HTML - which is a good point to note, not all URLs you load will return HTML code. In particular, this URL returns unicode encoded JSON (JavaScript Object Notation). (The unicode encoding implies that the MTA might be using python to generate these status updates, btw).

1. Verify that the response you get from calling the URL from XHR tab is the same as the response you get in python.
2. Import python's JSON module (it's a built in module, so no need to download it thru PyCharm) and convert your URL response to a python dict. (**[Documentation here](https://docs.python.org/3/library/json.html)**)
^^^ note that step 2 is equivalent to using `beautifulsoup` for parsing HTML...

Analyze the dict that you now have - does this look like the data that you need to build this script? Provide details to back up your stance.
