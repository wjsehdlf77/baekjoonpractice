#15988

from sys import stdin
 

t = int(stdin.readline())

data = []

for _ in range(t):
    data.append(int(stdin.readline()))

dp = [0] * (max(data) + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, max(data) + 1)






for i in data:
    print([dp[i]])


