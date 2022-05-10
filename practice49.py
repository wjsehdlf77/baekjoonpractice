#15988

from sys import stdin
 

t = int(stdin.readline())

data = []

for _ in range(t):
    data.append(int(stdin.readline()))

dp = [0] * (max(data) + 1)
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3

# for i in range(4, max(data) + 1)

def count(num):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    dp[num] = count(num - 1) + count(num - 2) + count(num - 3)
    

for i in data:
    count(i)
    print(dp[i])
    




# for i in data:
#     print([dp[i]])


