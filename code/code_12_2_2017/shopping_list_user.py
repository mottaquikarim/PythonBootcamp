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

