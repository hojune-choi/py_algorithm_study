#Sentinel Linear Search
#Linear Search의 cost를 반으로 줄일 수 있음

import random
import copy
from typing import Any, Sequence

def sentinel_linsearch(a: Sequence, key: Any) -> int:
    '''시퀀스 a에서 key와 값이 같은 원소 선형 검색(보초법)'''
    x = copy.deepcopy(a)
    x.append(key)
    i = 0
    while True:
        if x[i] == key:
            return i
        i += 1


if __name__ == '__main__':
    a = [None] * 10
    for j in range(10):
        a[j] = random.randint(0, 20)

    key = random.randint(0, 20)
    b = sentinel_linsearch(a, key)
    print(f'배열:{a} | 키:{key}')

    if b == len(a):
        print('배열에 키가 존재하지 않음')
    else:
        print(f'배열[{b}]에 위치')
