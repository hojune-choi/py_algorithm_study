#Greedy Algorithm - 잔돈 구하기

import random

def grd(n):
    coins = [500, 100, 50, 10]
    count = []
    for coin in coins:
        count.append(n // coin)
        n %= coin
    return count


n = 10 * random.randint(1, 500)
print(f'{n} - {grd(n)}')
