 n = int(input())

for i in range(n):
    li = input().split()
    h = int(li[0])
    w = int(li[1])
    num = int(li[2])
    
    floor = num % h
    room =  
    
    room = int((num // h) + 1)
    if room < 10:
        print(f'{floor}0{room}')
    else:
        print(f'{floor}{room}')

#미완성
#list comprehension 쓰면 쉽게 풀릴 것 같기도
