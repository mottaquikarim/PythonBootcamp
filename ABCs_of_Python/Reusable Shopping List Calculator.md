# Reusable Shopping List Calculator

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
