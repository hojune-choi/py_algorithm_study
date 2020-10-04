#Greedy Algorithm - law of large number

#주어진 수 M번 더하기
#K번 초과는 안됨

import random

def law_large(list1, list2):
    pass


list1 = [random.randint(2,1000), random.randint(1, 10000), random.randint(1, 10000)]
print(f'{list1}')
list2 = [None] * list1[0]
for i in range(list1[0]):
    list2[i] = random.randint(1, 10000)
print(f'{list2}')
