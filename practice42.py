#10162

from sys import  stdin

#A = 300, B = 60, C = 10
time = int(stdin.readline())

a = 0
b = 0
c = 0

while time > 0:
    if time >= 300:
        time -= 300
        a += 1
    elif time >= 60:
        time -= 60
        b += 1
    else:
        time -= 10
        c += 1
    
if time == 0:
    print(f"{a} {b} {c}")
else:
    print(-1)


