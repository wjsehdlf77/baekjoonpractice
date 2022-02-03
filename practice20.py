# 2753번

from sys import stdin

year = int(stdin.readline())

# 400의 배수
# 4의배수이면서 100의배수x
# 100의배수이면서 400의배수X


if year % 400 ==0:
    print(1)

elif (year % 4 == 0) and (year % 100 > 0):
    print(1)
else:
    print(0)

