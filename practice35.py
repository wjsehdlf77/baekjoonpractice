10988
from sys import stdin

word = list(stdin.readline().rstrip())

total = 0

for n in range(len(word) // 2):
    if word[n] == word[- (n + 1)]:
        total += 1
    
if total == len(word) // 2:
    print(1)
else:
    print(0)










