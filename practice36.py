#5086

from sys import stdin

data = []

while True:
    a = [int(n) for n in stdin.readline().split()]
    if a == [0, 0]:
        break
    data.append(a)

for i in range(len(data)):
    if data[i][0] % data[i][1] == 0:
        print("multiple")
    elif data[i][1] % data[i][0] == 0:
        print("factor")
    else:
        print("neither")


