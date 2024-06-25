s = input()

for i in 'abcdefghijklmnopqrstuvwxyz':
    print(s.find(i), end = ' ')


# 다른 방법   
S = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in S:
        print(S.index(i), end =' ')
    else:
        print(-1, end=' ')