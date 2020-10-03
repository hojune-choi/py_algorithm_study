# 1부터 n까지의 정수 합 구하기

def ssum(n):
    return n * (n + 1) // 2

n = int(input('n을 입력하세요: '))
print(f'1부터 {n}까지 정수 합은 {ssum(n)}입니다.')
