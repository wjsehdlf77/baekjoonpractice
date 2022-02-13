#2884번

from sys import stdin

H, M = map(int, stdin.readline().split())

if H  != 0:
    if M - 45 < 0:
        now_M = 60 - (45 - M)

        print(f'{H-1} {now_M}')
    else:
        print(f'{H} {M - 45}')
else:
    if M - 45 < 0:
        now_M = 60 - (45 - M)
        H = 23
        print(f'{H} {now_M}')
    else:
        H = 0
        print(f'{H} {M - 45}')