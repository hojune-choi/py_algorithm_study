#Binary Search
#Linear Search보다 빠름

import random
from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    '''시퀀스 a에서 key와 일치하는 원소 이진 검색'''
    fi = 0
    li = len(a) - 1

    while True:
        ci = (fi + li) // 2
        if a[ci] == key:
            return ci
        elif a[ci] < key:
            fi = ci + 1
        else:
            li = ci - 1
        if fi > li:
            break

    return -1


if __name__ == '__main__':
    a = [None] * 10
    for j in range(10):
        a[j] = random.randint(0, 20)

    a.sort()
    key = random.randint(0, 20)
    b = bin_search(a, key)
    print(f'배열:{a} | 키:{key}')

    if b == -1:
        print('배열에 키가 존재하지 않음')
    else:
        print(f'배열[{b}]에 위치')
