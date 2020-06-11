def calculation(a, b):
    li = []
    li.append(a * (b % 10))
    li.append(a * ((b % 100) // 10))
    li.append(a * (b//100))
    li.append(a*b)
    return li

a = int(input())
b = int(input())
li = calculation(a,b)
for i in li:
    print(i)


"""
함수의 return type이 list일때 다루는 방법
"""

