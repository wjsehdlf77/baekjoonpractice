#9056

from sys import stdin



while True:
    a = []
    data = int(stdin.readline())
    if data == -1:
        break
    for num in range(1, data):
        if data % num == 0:
            list.append(num)
        if sum(list) == data:
            print()
    

