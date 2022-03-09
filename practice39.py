#8958  

from sys import stdin

N = int(stdin.readline())

count = 0
total = 0

for _ in range(N):
    data = list(stdin.readline().rstrip())
    for i in range(len(data)):
        if data[i] == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)
    count = 0
    total = 0



