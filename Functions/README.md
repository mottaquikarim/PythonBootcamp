# Functions

A function is a reusable block of code that takes in inputs, operates on them and returns outputs. You can think of functions as a programmatic version of formulas.

## Example

```python
def area_of_circle(r):
  return 3.14 * r ** 2
  
```

In the example above, we define a **formula** for calculating the area of a circle. Now, we can **invoke** the function as often as we want to calculate area

```python
print(area_of_circle(1))
print(area_of_circle(2))
```

## Inputs

We define arguments to be the inputs that a function requires. Functions can require mutliple arguments.

```python
def avg_5(a,b,c,d,e):
  sum = a + b + c + d + e
  
  return sum / 5
  
print(avg_5(1,2,3,4,5)) # 7.5
```

## Optional Inputs

We can also define optional inputs

```python
def avg_5(a, b=0, c=0, d=0, e=0):
  sum = a + b + c + d + e
  
  return sum / 5
  
print(avg_5(1)) # 0.2
```

In this example, only ONE argument is required to be passed in, the rest default to 0.

## Outputs

What does this following function do?

```python
def foobar():
  print("hello")
  
foobar()
```


While it prints "hello" to the screen, it does not return anything! For a function to be useful, it must return a datatype. As demonstrated above, `return` keyword allows us to achieve this. We can also return multiple items:

```python
def increase_by_5(a,b):
  return a + 5, b + 5
  
c, d = increase_by_5(1,2) # c = 6, d = 7
```

## Conditionals

We can use booleans to "make decisions" within our code.

```python

if True:
  # this line will run

```

We use comparison operators in python within conditional statements

```python
a = 1
if a > 0:
  print(a)
  a + 1
```

The above will only run if `(a>0)` is true

We can do compound statements with `and` or `or` keywords

```python
if a > 0 and a % 2 == 0:
  # if a is a positive number and even
  
if a < 0 or a % 2 != 0:
  # if a is negative number and odd
```

We can use `is` keyword to check for equality

```python
if a is None:
  # runs if a is not yet defined
  
a = 1

if a is 1:
  # will run, since we set a to be 1
```



## 🚗 Practice: Shopping List Calculator IV

Builds off of [Shopping List Calculator III](https://github.com/mottaquikarim/Python101/blob/master/Basic_Data_Types/README.md#-practice-shopping-list-calculator-iii).

Write a function - **`get_item`** - that asks user for three inputs (from keyboard):

* `item_name`
* `item_price`
* `item_quantity`

It should print out: `{item_quantity} {item_name} = ${item_price}.` AND return the `item_price`.

Write another function - **get_total** that takes each `item_price` returned from previous **`get_item`** function and computes the total with tax.


## 🚗 Practice: Shopping List Calculator V

Write a function, **`within_budget`** that takes two arguments: `total` and `budget` and replies True or False based on whether `total` is greater than `budget`. `budget` should be an optional parameter that defaults to `None`


