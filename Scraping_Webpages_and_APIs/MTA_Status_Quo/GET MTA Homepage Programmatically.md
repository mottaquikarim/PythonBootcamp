# GET MTA Homepage Programmatically

We begin by exploring how we can fetch an HTML page programmatically like python. This functionality is similar to what your browser does everytime you navigate to a webpage from the URL bar.

## Python Libraries

Most programming languages have some sort of central area for shared libraries. A **library** is a collection of functions that are reusable for a wide variety of usecases. For example, writing the code necessary for making a programmatic call to a website is long winded and repetitious (ie: no matter which website you want to call, most of the code to *make* the call will be the same).

So of course, this can be turned into a function. And more importantly, this function (or, these series of functions) can be published such that *others* can use this functionality easily as part of their programs. 

To GET the MTA page programmatically, we will rely on pythons **[requests](http://docs.python-requests.org/en/master/)** library.

## Loading Python Dependencies

Loading dependencies is built in to PyCharm, which is nice because this allows us to avoid having to interact with the Terminal. It is also not-so-nice because the correct / proper way to install dependencies **is** to in fact use the Terminal.

That being said, to install a dependency with Pycharm, perform the following steps:

### 1. Navigate to Preferences in PyCharm

![1](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/Deps_Step1.png?raw=true)

### 2. Open up the Project Interpreter

![2](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/Deps_Step2.png?raw=true)

### 3. On the bottom left, click on the '+' button

(on the bottom left)
![3](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/Deps_Step3.png?raw=true)

### 4. In the search bar, look for the dependency you want, in this case `requests`, highlight and click 'Install Package'

![4](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/Deps_Step4.png?raw=true)

### 5. After it is downloaded, the dependency will be listed as 'installed'. Make note of the version number.

![5](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/Deps_Step5.png?raw=true)

### 6. If it doesn't exist, create a file called `requirements.txt` in your project root

### 7. In that file, add a new line that looks like this:

```
requests=[version_number_from_preferences]
```

At the time of this writing that version should look like:
```
requests=2.18.4
```

## Fetching MTA Homepage HTML

Using the documentation provided from the  **[requests](http://docs.python-requests.org/en/master/)** library, import the module into a new file and make a request to http://mta.info`. Your program should print out the raw HTML code for the homepage.
