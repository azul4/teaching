x = []
y = []
X, Y = 0, 0
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()

if x.count(max(x)) == 2:
    X = min(x)
else: X = max(x)

if y.count(max(y)) == 2:
    Y = min(y)
else: Y = max(y)


print("{} {}".format(X, Y))

"""
반드시 for _ in range(3)로 유도. -> 활용하지 않을 것이라는 확신.
아이디어는 1번만 나온 아이템을 다시 프린트한다.
이외의 직사각형 만들기 아이디어는?
"""
