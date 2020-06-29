li = [['1', 'Q', 'A', 'Z'],
      ['2', 'W', 'S', 'X'],
      ['3', 'E', 'D', 'C'],
      ['4', '5', 'R', 'T', 'F', 'G', 'V', 'B'],
      ['6', '7', 'Y', 'U', 'H', 'J', 'N', 'M'],
      ['8', 'I', 'K', ','],
      ['9', 'O', 'L', '.'],
      ['0', '-', '=', 'P', '[', ']', ';', "'", '/']
      ]

count = [0 for i in range(8)]

n = input()

for i in range(len(n)):
    test = n[i]
    for j in range(len(li)):
        if test in li[j]:
            count[j] += 1
            break

for i in count:
    print(i)

#영어문제
#리스트 활용
#'1QAZ', '2WSX'라고 표현해도 됐는데..
