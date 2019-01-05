# Meets Budget?

Ok, now that we have an easy to use, full functional shopping list calculator, let's make it **even more** useful!

* Create a function that takes in two arguments:
  * a list of tuples that represent shopping items and quantity
  * a max budget (number)
* If the budget is too low, return a list of items that **can** be purchased with the available funds. Remember, we want to maximize the number of items that are purchasable - how can that be achieved? 
  * (**Hint**: Google sorting lists of tuples)
* If the budget is exactly right, return an empty list
* If budget is higher than needed, return list with one time: the difference between budget and total_due

To solve this problem, you will have to leverage **conditional statements** which are how we teach a program to **make decisions**. Here are some resources on conditional statements: [resource](http://www.openbookproject.net/books/bpp4awd/ch04.html), [resource](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html).

Also an example:
```python
k = 8
if k < 9:
 print('It is!')
else:
 print('It is not!')
 
# etc
```

**Requirements**
```
Function name: get_shopping_list_price_from_list
Arguments:
  prices: (list)
  max_budget: number
Returns:
  list
```

**Sample Output**
```
[]
```

**Example Invocation**
```python
# budget too low
amt = get_shopping_list_price_from_list([('steak', 2), ('tomatoes', 1) ('redbull', 5), ('lentils', 4), ('orange juice', 1)], 2)
print(amt) # [('lentils', 4)]

# budget exactly right
amt = get_shopping_list_price_from_list([('steak', 2), ('tomatoes', 1) ('redbull', 5), ('lentils', 4), ('orange juice', 1)], 69.68)
print(amt) # []

# budget too hight
amt = get_shopping_list_price_from_list([('steak', 2), ('tomatoes', 1) ('redbull', 5), ('lentils', 4), ('orange juice', 1)], 70)
print(amt) # [0.32]

```
