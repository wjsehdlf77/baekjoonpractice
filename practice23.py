# 2480번

# 같은눈이 3개 10000+ 같은눈 * 1000

# 같은눈 2개 1000 + 같은눈*100

# 모두 다른눈은 가장큰눈* 100

# from sys import stdin

# num1, num2, num3 = map(int, stdin.readline().split())


# if num1 != num2 != num3:
#     price = max(num1, num2, num3)
#     print(price * 100)

# elif num1 != num2 or num2 != num3 or num1 != num3:
#     if num1 == num2:
#         price = (num1 * 100) + 1000
#         print(price)
#     elif num3 == num2:
#         price = (num3 * 100) + 1000
#         print(price)
#     elif num1 == num3:
#         price = (num1 * 100) + 1000
#         print(price)

# else:
#     price = (num1 * 1000) + 10000
#     print(price)



from sys import stdin

A, B, C = map(int, stdin.readline().split())

if A==B==C:
    print(10000 + A * 1000)

elif A==B:
    print(1000 + 100 * A)

elif A==C:
    print(1000 + 100 * A)

elif C==B:
    print(1000 + 100 * C)

elif A != B != C:
    print(100 * max(A, B, C))


















