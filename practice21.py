# 10039번

from audioop import avg


score =[]
total = 0

for num in range(5):
    A = int(input())
    score.append(A)
for num in range(0, 5):
    if score[num] < 40:
        score[num] = 40
for num in score:
    total += num
print(total // 5)

    

