from sys import stdin
from collections import deque


M, N = map(int, stdin.readline().split())


arr = [[0] * N for _ in range(M)]


x_now, y_now = 0, 0

check = 1

arr[0][0] = check

result = 0
queue = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])

while True:
    
    dy, dx = queue.popleft()
    y_now += dy
    x_now += dx
    
    if x_now >= N or x_now < 0 or y_now >= M or y_now < 0 or arr[y_now][x_now] != 0:
        result += 1
        y_now -= dy
        x_now -= dx
        queue.append((dy, dx))
    else:
        check += 1
        arr[y_now][x_now] = check
        queue.appendleft((dy, dx))
        

    if check == M*N:
        break

print(result)
print(y_now + 1, x_now + 1)





