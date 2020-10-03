# 10진수 정숫값을 입력받아 2~16진수로 변환하여 출력

import random

def card_trans(x: int, r: int) -> str:
    """정숫값 x를 r진수로 변환 후 문자열로 반환"""
    d = ''
    dchar = '0123456789ABCDEF'
    while x > 0:
        d += dchar[x % r]
        x //= r
    return d[::-1]

if __name__ == '__main__':
    r = random.randint(2, 16)
    x = random.randint(0, 100)

    print(f'{x}를 {r}진법으로 변환')
    print(f'-> {card_trans(x, r)}')
