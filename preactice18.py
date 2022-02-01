# 11653번


def a_prime_factor(num):


    for element in range(2, num + 1):
        while num % element ==0:
            num /= element
            print(element)

case = int(input())

a_prime_factor(case)





# while num % 2 ==0:
#     num /= 2
#     print(2)

# while num % 3 == 0:
#     num /= 3
#     print(3)






    