# Open-ended Shopping List Calculator with Quantity


Let's solve the above problem, but this time with the quantity of each item baked in. Remember, we want to leverage the `list` data structure to achieve this. However, we can/will **also** use the pythonic concept of a **tuple**.

Let's learn by example, checkout this how-to of working with/manipulating a tuple:

```python
my_tup = (5.45, 8)
# accessing the first item in a tuple
price = my_tup[0]
# access the last item in a tuple
quant = my_tup[1]
```

* Using tuples, **refactor** your `get_shopping_list_price_from_list` function to also account for quantities
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
amt = get_shopping_list_price_from_list([(4, 2), (0.75,, 1) (10, 5), (0.45, 4), (3.45, 1)])
print(amt) # 69.68
```
