from sys import stdin

num = int(stdin.readline().rstrip())
for i in range(num):
    for j in range(i):
        print('*', end=' ')
    print('')
for k in range(num, 0, -1):
    for l in range(k):
        print('*', end=' ')
    print('')
