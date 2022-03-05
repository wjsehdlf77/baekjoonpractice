#9610

from sys import stdin

N = int(stdin.readline())

data = []

for _ in range(N):
    data.append(list(map(int, stdin.readline().split())))

# Q1, Q2, Q3, Q4, Q5
count = [0]*5

for i in range(len(data)):
    if 0 in data[i]:
        count[4] += 1
    elif data[i][0] > 0 and data[i][1] > 0:
        count[0] += 1
    elif data[i][0] < 0 and data[i][1] > 0:
        count[1] += 1 
    elif data[i][0] < 0 and data[i][1] < 0:
        count[2] += 1
    else:
        count[3] += 1

print(f"""Q1: {count[0]}
Q2: {count[1]}
Q3: {count[2]}
Q4: {count[3]}
AXIS: {count[4]}""")

