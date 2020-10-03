# a부터 b까지 정수 합 구하기

def unk_sum(a, b):
    if a > b:
        a, b = b, a
    tot = 0
    for i in range(a, b + 1):
        tot += i
    return tot

a = int(input('정수 a: '))
b = int(input('정수 b: '))
print(f'{a}부터 {b}까지 정수 합은 {unk_sum(a, b)}입니다.')