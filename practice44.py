#10214

from sys import stdin

t = int(stdin.readline())


yon = 0

ko = 0

num = 0

for i in range(1, (t * 9) + 1):
    if i % 10 == 1:
        num += 1

    a, b = map(int, stdin.readline().split())
    yon += a
    ko += b
    if i % 9 == 0:
        if yon > ko:
            print("Yonsei")
        elif ko > yon:
            print("Korea")
        else:
            print("Draw")
        yon = 0
        ko = 0



# 1
# 1 0
# 0 0
# 0 0
# 0 0
# 0 0
# 0 0
# 0 0
# 0 0
# 0 0   