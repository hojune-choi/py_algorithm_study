# 넓이가 주어졌을 때, 직사각형 변의 길이 조합 구하기

def rect(area):
    alist = []
    for i in range(1, area + 1):
        if area % i:
            continue
        alist.append([i, area // i])
    return alist

area = int(input('직사각형의 넓이를 입력하세요.: '))
print(f'{rect(area)}')