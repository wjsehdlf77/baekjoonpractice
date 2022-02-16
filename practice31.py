#7567

# (이게 정상적으로 놓은거

# )이게 반대로 놓인것\

# 그릇을 포개면 5cm 그릇이 반대면 10cm

from sys import stdin

plate = list(stdin.readline().rstrip())

height = 10
for n in range(len(plate) - 1):
    if plate[n] != plate[n + 1]:
        height += 10
    else:
        height += 5

print(height)




