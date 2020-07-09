T = int(input())
for i in range(T):
    sent = input().split()
    for j in sent:
        print(j[::-1], end = ' ')
    print()
        


# str[::-1] 
