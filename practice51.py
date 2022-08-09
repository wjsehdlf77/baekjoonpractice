#1913

from sys import stdin as st

N = int(st.readline())
want = int(st.readline())
list = [[0] * N for _ in range(N)]
x_now, y_now = 0, 0; x_want, y_want = 0, 0; x, y = [0, 1, 0, -1], [1, 0, -1, 0]
num = N**2 - 1
list[y_now][x_now] = N**2

while True:
    for i in range(0, 4):

        while True:
            
            x_now += x[i]
            y_now += y[i]
            if x_now < 0 or y_now < 0 or x_now >= N or y_now >= N or list[y_now][x_now] != 0:
                x_now -= x[i]
                y_now -= y[i]
                break
            else:
                list[y_now][x_now] = num
                if list[y_now][x_now] == want:
                    x_want, y_want = x_now, y_now
                num -= 1
                print(y_now, x_now)

    if x_now == N//2 and y_now == N//2: break
for i in list:
    print(*i)
print(y_want + 1, x_want + 1)

0 ,5
1, 5

        







    
        

# 1, 1부터 밑으로 탐색
# 밑에서부터 시계반대방향으로 0 탐색

# [[9, 2, 3],[8, 1, 4],[7, 6 ,5]]

# 7
# 35

