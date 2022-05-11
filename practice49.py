#15988

from sys import stdin


def count(data):
    dp = [0] * (data + 1)
    
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    if dp[data] != 0:
        return 0
    return count(data - 1) + count(data - 2) + count(data - 3)

    

t = int(stdin.readline())

for _ in range(t):
    data = int(stdin.readline())
    print(count(data))
    




    





# 3
# 4
# 7
# 10