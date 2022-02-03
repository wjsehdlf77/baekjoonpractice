# 1934번
from sys import stdin

test_case = int(stdin.readline())
            

for a in range(test_case):
    num1, num2 = map(int, stdin.readline().split())
    
    multi = num1 * num2

    for a in range(min(num1, num2), 0 ,-1):
        if (num1 % a == 0) and (num2 % a == 0):
            print(multi // a)
            break



