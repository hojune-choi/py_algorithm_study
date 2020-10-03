# 시퀀스 원소를 역순으로 정렬하기

import random
from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> Any:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
    return a

if __name__ == '__main__':
    rarray = [None] * 5
    for i in range(5):
        rarray[i] = random.randint(0, 100)

    print(f"기존 배열: {rarray}")
    print(f"역정렬: {reverse_array(rarray)}")
