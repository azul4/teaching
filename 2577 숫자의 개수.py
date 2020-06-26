#1 list comprehension을 배우지 않았을 경우.

a = int(input())
b = int(input())
c = int(input())

num = list(str(a*b*c))
li = [0,0,0,0,0,0,0,0,0,0]
for i in num:
    li[int(i)] += 1

for i in range(10):
    print(li[i])
    
#2 list comprehension을 배웠으나 pythonic하지 않은 경우.
import math

a = int(input())
b = int(input())
c = int(input())

num = a*b*c
strnum = str(num)
length = int(math.log10(num)) + 1
li = [0 for i in range(10)]
for i in range(length):
    li[int(strnum[i])] += 1

for i in range(10):
    print(li[i])
