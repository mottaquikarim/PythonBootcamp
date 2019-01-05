# With Coupons

Update our function to take a list of price markups or markdowns. For example:

* we can now count **sales tax** as a markup (since it increases total due)
* we can count a coupon as a markdown (since it decreases total due)

You function will assume the first item in the list is tax markup. It should support at most 4 more coupon markdowns after that first item.

Remember, all coupons should be applied **before** taxes are applied. Additionally, if the markdowns render amount due to be less than 45% of the total before any price transformations, render all subsequent markdowns invalid.


**Requirements**
```
Function name: get_shopping_list_price_from_list
Arguments:
  prices: (list)
  tforms: (list)
Returns:
  number
```

**Sample Output**
```
8
```

**Example Invocation**
```
amt = get_shopping_list_price_from_list([('steak', 2)], [0.08875, 0.25, 0.15])
print(amt) # 5.55

amt = get_shopping_list_price_from_list([('steak', 2)], [0.08875])
print(amt) # 8.71

amt = get_shopping_list_price_from_list([('steak', 2)], [0.08875, 0.25, 0.15, 0.15, 0.15])
print(amt) # 4.01

amt = get_shopping_list_price_from_list([('steak', 2)], [0.08875, 0.25, 0.15, 0.15, 0.15, 0.98])
print(amt) # 4.01 - just ignore the 6th markdown

amt = get_shopping_list_price_from_list([('steak', 2)], [0.08875, 0.25, 0.15, 0.95, 0.25])
print(amt) # 5.55 - ignore everything after the 15% off because drives price below 45% of original price
```

