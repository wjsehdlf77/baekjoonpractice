#16234

from sys import stdin

n, l, r = map(int, stdin.readline().split())

data = []
day = 0

x = [1, -1, 0, 0]
y = [0, 0, 1, -1]

for _ in range(n):
    row = list(map(int, stdin.readline().split()))

    data.append(row)

while True:
    for i in range(3):
        
