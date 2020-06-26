n = int(input())
li = list(map(int, input().split()))
tot = 0
for i in li:
    tot += i / max(li) * 100

print(tot / n)
    
#map과 list 적절히 섞어쓰기 좋은 문제
#map은 학생이 int(input()) 표현에 환멸을 느낄 때 즈음에 
