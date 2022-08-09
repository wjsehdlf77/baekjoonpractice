#11060

from sys import stdin

N = int(stdin.readline())

data = [int(a) for a in stdin.readline().split()]

save = [0] * N 

save[0] = 1

def finish():
    