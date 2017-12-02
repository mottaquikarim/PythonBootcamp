# def get_shopping_list_price(sp, sc, tp, tc, rp, rc, lp, lc, ojp, ojc):
#     sum = sp*sc + tp*tc + rp*rc + lp*lc + ojp*ojc
#     tax = 0.08875
#     total_due = sum * (1 + tax)
#
#     return total_due
#
# sA = get_shopping_list_price(4, 1, 0.75, 1, 10, 1, 0.45, 1, 3.45, 1)
# print(sA)
#
# sB = get_shopping_list_price(5, 1, 0.75, 1, 9, 1, 0.45, 1, 3.45, 1)
# print(sB)

def get_shopping_list_price(price_list):
    sum = 0
    for item in price_list:
        sum += item

    tax = 0.08875
    total_due = sum * (1 + tax)

    return total_due

def get_shopping_list_price_and_q(price_list):
    sum = 0
    for item in price_list:
        price = item[0]
        q = item[1] or 1
        sum += float(price)*float(q)

    tax = 0.08875
    total_due = sum * (1 + tax)
    return total_due

print(get_shopping_list_price_and_q([(4.5, 1), (10, 1), (0.75,4)]))

sA = get_shopping_list_price([4, 0.75, 10])
print(sA)

sB = get_shopping_list_price([5, 0.75, 9, 0.45, 3.45])
print(sB)

# downsides: what if keys dont exist?
[{
    'price': 4,
    'q': 2,
}, {
    'price': 0.75,
    'q': 1,
}, {
    'price': 10,
    'q': 1,
}]

# misaligned data
prices = [4.5, 1, 10]
q = [1,3]

# list of lists
[(4.5, 1), (10, 1), (0.75,4)]

# EXAMPLES OF HOW LIST WORKS...
grades = [100, 98, 67]
# print(grades)
grades.append(89)
grades_len = len(grades)
# print(grades[grades_len-1])

count = 0
for grade in grades:
    # print(grade)
    if grade > 85:
        count += 1 # count = count + 1

# print(count)

# LIST COMPREHENSIONS!

curved = [grade*1.05 for grade in grades if grade < 85]
# print(curved)