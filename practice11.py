# 2530번

A, B, C = map(int, input().split())
D = int(input())

seconds = D + C

while seconds >= 60:
    seconds -= 60
    B += 1

while B >= 60:
    B -=60
    A += 1

while A >= 24:
    A -= 24

print(f'{A} {B} {seconds}')


    


    
    