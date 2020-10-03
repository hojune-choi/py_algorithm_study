# n까지의 소수 구하기

import random

def prime_ls(n):
    alist = []
    for num in range(2, n+1):
        if all(num % elem != 0 for elem in range(2, num)):
            alist.append(num)
    return alist


if __name__ == '__main__':
    n = random.randint(0, 1000)

    print(f'1부터 {n}까지의 소수: {prime_ls(n)}')
