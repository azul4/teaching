a, b = map(int, input().split())

word = input().split()

count = 0

for i in word:
    count += len(i)
    if count <= b:
        print(i, end=' ')
    else:
        print()
        count = len(i)
        print(i, end = ' ')
        
## 영어어문제
## print("sentence", end='') 배우고 난 다음에 활용
## for loop도.
    
