# 🙌 🙌 Interactive Shopping Budgeter

 **We did it!** We have a pretty solid program built...
 
 Now, let's put this into overdrive. In python we can define what is called a **Class** that helps us maintain state on information that is being added to or removed. Let's take advantage of that to create a Shopping Budgeter class that will keep track of competitor prices, allow us to create a shopping list, and suggest to us where we should go to get the best prices. 
 
 Here is how we can create classes in python:
 
 ```python
 class Cat():
 
  def __init__(self, name):
   self.name = name
   self.age = 0

  def speak():
   print('meow')

  def birthday();
   self.age += 1

  def __str__():
   return "{}, {}".format(self.name, self.age)
 ```

Usage:

```
belle = Cat('Annabelle Lee')
belle.speak() # meow
belle.birthday() 
belle.birthday() 
print(belle) # Annabelle Lee, 2
```

Using the python `input` command, ask a user to list out items and quantities to purchase and a budget. Internally, track a few stub competitors with their own prices for items.

Based on user input, suggest a competitor that would offer the most savings.
