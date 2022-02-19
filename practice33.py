#10102


from sys import stdin

V = int(stdin.readline())
vote = list(stdin.readline().rstrip())
A_vote = 0

for n in range(V):
    if vote[n] == 'A':
        A_vote += 1

if A_vote > (V / 2):
    print('A')
elif A_vote < (V / 2):
    print('B')
else:
    print('Tie')




