# Meets Budget?

Ok, now that we have an easy to use, full functional shopping list calculator, let's make it **even more** useful!

* Create a function that takes in two arguments:
  * a list of tuples that represent shopping items and quantity
  * a max budget (number)
  
If the budget is too low, return a list of items that **can** be purchased with the available funds. Remember, we want to maximize the 

Now, let's suppose we want to abstract away the need to have to code in **prices** of our shopping items by hand. How could we achieve such a thing?

As it turns out, python supports the concept of a **dictionary** data structure for specifically this purpose. Consider the following:

```python
gradebook = {
  'Normal Person': 85,
  'Really Smart Person': 100,
  'A Solid B is OK Son': 81,
  'Taq Karim': 98, # 😭 my mother would consider this failing
  'Some Rebel': 45, # 😎 she doesn't play by the rules
}
```
We call this a dictionary. Dictionaries are made of **keys** - the text wrapped in quotes and **values** - in this case, numbers. The values of a dictionary can be any valid pythonic data type, this includes text, numbers, lists, tuples, and yes - other dictionaries too!

```python
# super quick example of a dictionary of dictionaries in python

dictionary = {
  'A': {
    'abed': 'adv. In bed; on a bed. ',
    'aberration': 'n. Deviation from a right, customary, or prescribed course. ',
    'abet': 'v. To aid, promote, or encourage the commission of (an offense). ',
    'abeyance': 'n. A state of suspension or temporary inaction. ',
  },
  'B': {
    ...
  },
  ...
  'Z': {
    'zealot': 'n. One who espouses a cause or pursues an object in an immoderately partisan manner. ',
    'zeitgeist': 'n. The intellectual and moral tendencies that characterize any age or epoch. ',
    'zenith': 'n. The culminating-point of prosperity, influence, or greatness. ',
    'zephyr': 'n. Any soft, gentle wind. ',
    'zodiac': 'n. An imaginary belt encircling the heavens within which are the larger planets.  ',
  }
}
```

Anyways, I digress. Let's define the shopping items for our supermarket and their corresponding prices as a dictionaryy. Then, let's update our function to reference the **key** of the dictionary instead of the price of the item.

* Create a **dictionary** called `inventory` that lists a bunch of items and their prices.
* Modify our shopping list function to consume a tuple consisting of a **string** and a **number**, effectively `('name_of_item', quantity_of_item)` and ensure the return value is the same.

**Requirements**
```
Function name: get_shopping_list_price_from_list
Arguments:
  prices: (list)
Returns:
  number that represents total_due
```

**Sample Output**
```
69.68
```

**Example Invocation**
```python
amt = get_shopping_list_price_from_list([('steak', 2), ('tomatoes', 1) ('redbull', 5), ('lentils', 4), ('orange juice', 1)])
print(amt) # 69.68
```
