#세 정수 입력받아 중앙값 구하기

def med3(a, b, c):
    if (b >=  a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    else:
        return c
    

print('세 정수를 입력하시오.')
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))

print(f'중앙값은 {med3(a, b, c)}입니다.')