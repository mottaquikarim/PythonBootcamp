# LOOK MA! this is a comment

'''
LOOK AM!
    this
        is
            ....python
'''

def format_as_price(price):
    formatted = "%.2f" % price
    return formatted

# THIS IS OUR EXPECTED OUTPUT
'''
steak: $4.00/lb
tomatoes: $0.75/lb
redbull: $10.00
lentils: $0.45/lb
orange juice: $3.45
----------------------
sum: $18.65
total_due: $20.31
'''

# APPROACH 1
steak = 4
tomatoes = 0.75
redbull = 10
lentils = 0.45
orange_juice = 3.45

sum = steak + tomatoes + redbull + lentils + orange_juice
tax = 0.08875
total_due = sum * (1 + tax)

# TAX APPROACH 2
total_due = tax * sum + sum

# DIFFERENT WAYS TO PRINT
print('steak: $' + format(steak, '.2f') + '/lb')
print('steak: ${}/lb {} {}'.format(steak, 1, 2))

output = '''
steak: ${}/lb
tomatoes: ${}/lb
redbull: ${}
lentils: ${}/lb
orange juice: ${}
----------------------
sum: $18.65
total_due: $20.31
'''.format(format_as_price(steak), tomatoes, format_as_price(redbull), lentils, orange_juice)

print(output)
