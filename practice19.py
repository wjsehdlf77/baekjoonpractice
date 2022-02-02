#1789번

from sys import stdin

num = int(stdin.readline())

count = 1

while count * (count + 1)/2 <= num :
    count += 1
print(count - 1)


# from sys import stdin

# num = int(stdin.readline())

# count = 0

# for a in range(1, num + 1):
#     if num >= a:
#         num -= a
#         count += 1

# print(count)

# 이방법이 더 좋은 거 같은데... 시간초과
        




    
        