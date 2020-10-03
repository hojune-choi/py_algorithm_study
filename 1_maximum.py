#세 정수 입력받아 최댓값 구하기

def max3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print('세 정수를 입력하시오.')
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))

print(f'최댓값은 {max3(a, b, c)}입니다.')