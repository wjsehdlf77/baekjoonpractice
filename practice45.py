#11557

from sys import stdin

t = int(stdin.readline())

name_data = {}

max_data = 0

for _ in range(t):
    n = int(stdin.readline())
    for i in range(n):
        name, data = stdin.readline().split()
        name_data[int(data)] = name
    
        max_data = max(max_data, int(data))
    print(name_data[max_data])

        


# 2
# 3
# Yonsei 10
# Korea 10000000
# Ewha 20
# 2
# Yonsei 1
# Korea 10000000