# Compare Markets

Now, let's hook up our function to also compare markets. Essentially, now we will define **two** dicts which reflect inventory and pricing for two competing supermarkets.

For example:

```python
bobs_supermarket = {
 'item A': 2,
 'item B': 3,
}

janes_supermarket = {
 'item A': 3,
 'item B': 1
}
```

Our function will take our list of tuples, but also **two** dictionaries representing our two competitors. It will create **two** sums and return a dictionary that looks like the following:

```python
{
 'winner': 'competitor1',
 'savings': 1
}
```

Where **winner** refers to which competitor was cheaper and **savings** refers to how much money was saved.

**Requirements**
```
Function name: get_shopping_list_price_from_list
Arguments:
  prices: (list)
  c1: (dict) # first competitor
  c2: (dict) # second competitor
Returns:
  dict
```

**Sample Output**
```
{
 'winner': 'competitor1',
 'savings': 1
}
```

**Example Invocation**
```python
bobs_supermarket = {
 'item A': 2,
 'item B': 3,
}

janes_supermarket = {
 'item A': 3,
 'item B': 1
}
amt = get_shopping_list_price_from_list([
 ('steak', 2),
 ('tomatoes', 1),
 ('redbull', 5), 
 ('lentils', 4), 
 ('orange juice', 1)
], bobs_supermarket, janes_supermarket)
print(amt) # {'winner': 'competitor1','savings': 1}
```

## Challenges

1. Update your function so that it takes a list of competitors (ie: N competitors) and not just two
2. Add the budget field back and return a dictionary that chooses the competitor that saves you the most. If budget is too low for all competitors, return the competitor that allows you to get the most bang for your buck (ie: buy the most items)
