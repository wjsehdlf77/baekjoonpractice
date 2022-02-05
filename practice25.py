# 10156번
from sys import stdin
price, num, money = map(int, stdin.readline().split())

all_price = price * num

if all_price - money > 0:
    print(all_price - money)
else:
    print(0)
    