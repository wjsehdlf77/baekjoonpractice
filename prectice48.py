#10998, 1000, 1001, 1008

from sys import stdin

a, b = map(int, stdin.readline().split())

print(a/b)

#10869

from sys import stdin

a, b = map(int, stdin.readline().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

#10340

a, b, c = map(int, stdin.readline().split())

print((a + b) % c)
print(((a + c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)

#2588
a = int(stdin.readline())
b = stdin.readline().rstrip()
sum = a * int(b)
b = list(b)

for i in reversed(b):
    print(int(i)* a)

print(sum)

