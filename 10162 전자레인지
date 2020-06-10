def minimum(num):
    min5 = 0
    min1 = 0
    sec10 = 0
    if (num % 60) % 10 != 0:
        return -1
    while num >= 300:
        min5 += 1
        num -= 300
    while num >= 60:
        min1 += 1
        num -= 60
    sec10 += num // 10
    return [min5, min1, sec10]


n = int(input())
li = minimum(n)
if type(li) == int: print(li)
else :
    for i in li:
        print(i, end= ' ')

"""
함수의 접근, list의 return
"""
