#10103

from sys import stdin

round = int(stdin.readline())

dice = []

person1 = 100

person2 = 100

for _ in range(round):
    a, b = map(int, stdin.readline().split())

    dice.append([a, b])

for a, b in dice:
    

    if a > b:
        person2 -= a
    elif a < b:
        person1 -= b

print(person1)
print(person2)

