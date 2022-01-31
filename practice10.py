
A, B = map(int, input().split())
C = int(input())

C_B_hour = (C + B) // 60
C_B_minute = (C + B) % 60

A_day = (A + C_B_hour) // 24

A_hour = (A + C_B_hour) % 24

if A_day == 0:
    print(f'{A + C_B_hour} {C_B_minute}')

elif A_day > 0:
    print(f'{A_hour} {C_B_minute}')
    
    
    




