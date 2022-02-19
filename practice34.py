# 10886

from sys import stdin

N = int(stdin.readline())

vote_list = []

for _ in range(N):
    vote = int(stdin.readline())

    vote_list.append(vote)

if vote_list.count(0) > vote_list.count(1):
    print("Junhee is not cute!")
elif vote_list.count(0) < vote_list.count(1):
    print("Junhee is cute!")

