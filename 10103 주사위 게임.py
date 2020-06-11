n = int(input())
changyoung = 100
sangduck = 100
for i in range(n):
    c, s = map(int, input().split())
    if c>s:
        sangduck -= c
    elif c<s:
        changyoung -=s

print(changyoung)
print(sangduck)

#그냥 재미난 문제
