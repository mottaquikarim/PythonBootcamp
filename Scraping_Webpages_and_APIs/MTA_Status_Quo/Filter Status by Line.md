# Filter Status by Line

Now, let's write a function that will help us drill down even further. Your function should take two inputs:

1. dict of isolated subway line statues
2. list of subway lines to filter by

For example:

```python
lines = filter_by_lines({'ACE': 'Delays', 'L': 'LOL fckked', ..., 'S': 'Service Change'}, ['A', 'S'])
print(lines) # {'ACE': 'Delays', 'S': 'Service Change'), note that 'L' is no longer in the list
```

In order to pull this off, google `iterating through items in dict, python`
