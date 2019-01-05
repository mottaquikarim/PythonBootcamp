# (More Useful) Shopping List Calculator



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

## Code Sample
```python

def format_as_price(price):
    formatted = "%.2f" % price
    return formatted

steak = 4
tomatoes = 0.75
redbull = 10
lentils = 0.45
orange_juice = 3.45

formatted_steak = format_as_price(steak)
print('steak: ${}/lb'.format(formatted_steak))
quantity = input('how many lbs? -->')
steakq = int(quantity)
print('Ok {}lbs of steak'.format(steakq))
print(steak * steakq)

```

More complete example:

```python
def format_as_price(price):
    formatted = "%.2f" % price
    return formatted

def read_line(price, label, suffix='/lb'):
    fmt_price = format_as_price(price)
    print('{}: ${}{}'.format(label, fmt_price, suffix))
    quantity = input('how many {}? -->'.format(suffix))
    try:
        q = int(quantity)
    except ValueError:
        q = 1

    print('Ok {}{} of {}'.format(q, suffix, label))
    return q

steak = 4
tomatoes = 0.75
redbull = 10
lentils = 0.45
orange_juice = 3.45

steakq = read_line(steak, 'steak')
print(steak * steakq)

tomatoesq = read_line(tomatoes, 'tomatoes')
print(tomatoes * tomatoesq)

sum = steak*steakq + tomatoes*tomatoesq
tax = 0.08875
total_due = sum * (1 + tax)
print(sum, total_due)

```
