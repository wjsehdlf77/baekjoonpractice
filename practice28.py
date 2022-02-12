#2476번


from sys import stdin

test_case = int(stdin.readline())

price = []


for case in range(test_case):
    A, B ,C = map(int, stdin.readline().split())

    if A==B==C:
        price.append(10000+A*1000)
    elif A==B:
        price.append(1000+A*100)
    elif A==C:
        price.append(1000+A*100)
    elif C==B:
        price.append(1000+C*100)
    elif A != B != C:
        top_num = max(A,B,C)
        price.append(top_num*100)


print(max(price))
