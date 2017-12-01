# ABCs of Python

We will begin by exploring some of the basics of the python programming language. For example, how can we keep track of data in python? How does decision making work? Can we automate functionality so that we don't have to repeat ourselves? These are just some of the questions we'll tackle in this unit.

## Rules of Engagement
For all exercises, partner with someone next to you. Coding is **collaborating**. Talk through each problem and attempt to arrive at the solution **together**. Remember, it's ok to break stuff and get things wrong, that's the **only** way to learn!


## THEME: Death and Taxes

🎉🎈🎂🍾🎊🍻💃

We are a new startup! Cool! Our product has to do with tax calculation and other related financial services. In this unit, we will grow as a team, ramping up our python skills as we build our final product.

### 1. Simple Shopping List Calculator

Let's begin by building a simple shopping list. 

* Create a new file, `shopping_list.py`
* Create **5 variables** in python that store prices for items at the supermarket. 
* Write some code that will **sum** the prices of these items, store into a variable called `sum`
* Assuming NYC sales tax (8.875%), create another variable, `total_due` that represents how much our shopper owes. 

**Not sure where to begin??** Get used to it fam, that's 80% of programming! Here's [some cheatsheets](https://ehmatthes.github.io/pcc/cheatsheets/README.html) tho.

**Sample output**
```
steak: $4.00/lb
tomatoes: $0.75/lb
redbull: $10.00
lentils: $0.45/lb
orange juice: $3.45
----------------------
sum: $18.65
total_due: $20.31
```

By sample output I mean that your program should print out something similar to what I have there above.


### 2. (More Useful) Shopping List Calculator


Ok so our prototype is done! It works! Let's make it more useful. Specifically, let's try to solicit **user input** as part of our program.

* Create a new file, `shopping_list_user.py`
* Pull over the **5 variables** from `shopping_list.py`.
* Now, for each shopping item, **ask the user** how many of the items s/he would like to purchase.
* Find the sum now with user preferences in mind.
* Find total owed based off of sum.

**Sample output**
```
steak: $4.00/lb
how many lbs? -->
Ok, 2lbs of steak.

tomatoes: $0.75/lb
how many lbs? -->
Ok, 1lbs of tomatoes.

redbull: $10.00
how many? -->
Ok, 5 containers of redbull.

lentils: $0.45/lb
how many lbs? -->
Ok, 4lbs of lentils.

orange juice: $3.45
how many? -->
Ok, 1 bottles of orange juice.

----------------------
sum: $64.00
total_due: $69.68
```

### 3. Reusable Shopping List Calculator

We're not here to build usable products, fam.

* Take the code you wrote above and turn it into a **function**, which will make the logic reusable.
* (Here's some documentation on [python functions](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html). Here's a [tutorial](https://www.tutorialspoint.com/python/python_functions.htm))

**Example**
```python
# here is an example of a function, to help put in context

def c_to_f(celsius):
  faren = celsius * 1.8 + 32
  return faren
  
def get_full_name(firstname, lastname, middlename=""):
  fullname = firstname + ' ' + middlename + ' ' + lastname
  return fullname
  
# EXAMPLE INVOCATIONS 
  
print(c_to_f(0)) # 32
print(c_to_f(100)) # 212

print(get_full_name('Mottaqui', 'Karim', 'Al') # Mottaqui Al Karim
print(get_full_name('Taq', 'Karim') # Taq Karim
```

**Requirements**
```
Function name: get_shopping_list_price
Arguments:
  steak_p: (number) - price of steak
  steak_c: (number) - how many?
  tomaotoes_p: (number)
  tomaotoesp_c: (number)
  redbull_p: (number)
  redbull_c: (number)
  redbull_p: (number)
  redbull_c: (number)
  orangejuice_p: (number)
  orangejuice_c: (number)
Returns:
  number that represents total_due
```

**Sample Output**
```
69.68
```


## 🚗 Parking Lot

Interesting/useful links!

* [Cheatsheets](https://ehmatthes.github.io/pcc/cheatsheets/README.html)
* [Solicit User Input from Commandline](https://docs.python.org/3/library/functions.html#input)
* Functions! [this](https://www.tutorialspoint.com/python/python_functions.htm) and [this](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html)
