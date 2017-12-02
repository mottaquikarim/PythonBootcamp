steak = 4
tomatoes = 0.75
redbull = 10
lentils = 0.45
orange_juice = 3.45

sum = steak + tomatoes + redbull + lentils + orange_juice
tax = 0.08875
total_due = sum * (1 + tax)

def get_shopping_list_price(sp, sc, tp, tc, rp, rc, lp, lc, ojp, ojc):
    sum = sp*sc + tp*tc + rp*rc + lp*lc + ojp*ojc
    tax = 0.08875
    total_due = sum * (1 + tax)

    return total_due

sA = get_shopping_list_price(4, 1, 0.75, 1, 10, 1, 0.45, 1, 3.45, 1)
print(sA)

sB = get_shopping_list_price(5, 1, 0.75, 1, 9, 1, 0.45, 1, 3.45, 1)
print(sB)