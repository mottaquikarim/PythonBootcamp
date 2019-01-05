# Open-ended Shopping List Calculator


Let's tweak our `get_shopping_list_price` function to be more open ended.

Here's an important question: what if our shopping list wasn't just 5 items?

Let's examine the `list` data structure in python and see how we can leverage that to make our code even more useful. Additionally, you will have to look up **looping** to successfully solve this problem.

* Update the `get_shopping_list_price` function to accept one argument, a list that stores the prices of shopping list items
* Return the `total_due`

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
amt = get_shopping_list_price_from_list([4, 0.75, 10, 0.45, 3.45])
print(amt) # 20.31
```
