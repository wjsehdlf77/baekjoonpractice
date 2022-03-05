#5717

from sys import stdin

data = []

while True:
    a = [int(n) for n in stdin.readline().split()]
    if a == [0, 0]:
        break
    data.append(a)

for i in range(len(data)):
    a = sum(data[i])
    print(a)