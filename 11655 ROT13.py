#

def print_list(li):
    for i in li:
        print(i, end='')

        
alphabet_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_small = 'abcdefghijklmnopqrstuvwxyz'
big = 65
small = 97
n = list(input())

for i in range(len(n)):
    if n[i] in alphabet_small:
        n[i] = alphabet_small[(k+12)%len(n)]
    elif n[i] in alphabet_big:
        k = alphabet_big.index(n[i])
        n[i] = alphabet_big[(k+12)%len(n)]
    else:
        pass

print_list(n)
