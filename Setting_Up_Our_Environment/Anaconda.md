# Running Python Locally

Before we get into writing our code, we will have to install a few programs and tools. It may take about a half hr to pull off but ultimately a properly established development environment will pay off in spades as we navigate the rest of our day.

## Tools to Download

We will need to download two programs today. Links to download below.

### **[Anaconda](https://www.anaconda.com/download/)**
Anaconda is a free python environment. This program is **LARGE** and mainly unnecessary. However setting up with it does seem simple: just download, wait a billion minutes and **BOOM**, python is installed. Feel free to delete after class is over.

### **[PyCharm](https://www.jetbrains.com/pycharm/download/)**
**⚡⚡ BE SURE TO DOWNLOAD THE COMMUNITY EDITION ⚡⚡**.

PyCharm is an IDE (integrated development environment) that will allow you to write and run your python code in one simple program. Again, ideally we'd want to be able to do this in a more "regular" way (ie: via command line) but due to time restrictions and the beginner nature of this class, it is much simpler and easier to just go this route. 

## Connecting Anaconda and PyCharm

Anaconda kinda sucks for doing just pure, basic coding. They have a bunch of (tbf, cool looking) tools that you are free to explore after class...but we are here today to learn to code. As such, we cannot *only* use Anaconda, I find their UX to be painful and annoying for the simple usecases (ie: write some code, run the code, view the output, repeat).

So, we will be using **PyCharm** to **write** and **run** our python programs. However, we need PyCharm to point to **Anaconda** because that's where python is **"installed"**. Luckily, there seems to be good support for this. Follow the instructions below to get started.

### 1. Create New PyCharm Project.

Open PyCharm, run through their configs (ok to just use defaults, that's what I did). Then, go to **File>New Project**.

### 2. Point Project Interpreter to Anaconda

Use this **[handly tutorial](https://docs.anaconda.com/anaconda/user-guide/tasks/integration/pycharm)** from the Anaconda Documentation to associate PyCharm and Anaconda.

### 3. Run Sample Code

Now, let's write our first line of python! First, create a new file in project. Name the file `app.py`

![new_file](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/PyCharm_New_File.png?raw=true)

Then, write the following line of code:

```python
print('Hello, Wrold!')
```

Finally, run your code and ensure that you see the `Hello, Wrold` output as expected.

![run_code](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/PyCharm_Run_File.png)

![verify](https://github.com/mottaquikarim/PythonBootcamp/blob/master/assets/PyCharm_Verify_Output.png?raw=true)

## Setting up PythonAnywhere Account

Although wrangling the PyCharm / Anaconda set up described above will allow us to safely and happily write python code **locally**, it is in some ways severely limiting because we are not able to run long standing processes or communicate with our code from real world inputs.

In order to truly achieve freedom to do anything we want with python, we must configure an environment in the **cloud** that is accessible via the internet.

Normally, this is an expensive and skills-intensive process. But! The Future is Now fam, and our service based economy affords us the ability to relatively easily set up a python environment for experimenting around in the cloud for **free**(...mium).

Pls go to **[Python Anywhere](https://www.pythonanywhere.com/)** and create a free account. If you find the service useful, feel free to upgrade later. For now, just create the account and verify that you can log in. We will have instructions for transferring some of our projects to the internets later on in the day.


## 🚗 Parking Lot

Just some interesting/useful links I found while prepping for this class...

1. [Adding Packages to PyCharm Project](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)
