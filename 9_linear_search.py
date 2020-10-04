#Linear Search(선형검색)

"""
선형으로 늘어선 배열에서 원하는
키값을 가진 원소를 찾을 때 까지
맨 앞부터 스캔하여 순서대로 검색
"""

import random
from typing import Any, Sequence

def lin_search(a: Sequence, key: Any) -> int:
    '''시퀀스 a에서 key와 값이 같은 원소 선형 검색'''
    i = 0
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1


if __name__ == '__main__':
    a = [None] * 10
    for j in range(10):
        a[j] = random.randint(0, 20)

    key = random.randint(0, 20)
    b = lin_search(a, key)
    print(f'배열:{a} | 키:{key}')

    if b == -1:
        print('배열에 키가 존재하지 않음')
    else:
        print(f'배열[{b}]에 위치')
