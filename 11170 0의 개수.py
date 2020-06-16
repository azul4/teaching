n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    zeros = 0
    for j in range(a, b+1):
        str_j = list(str(j))
        for k in str_j:
            if k == '0':
                zeros += 1
    print(zeros)


"""
실질적으로 range(n, m) 꼴을 써볼 수 있는 기회
3중for문으로 속도 
"""
