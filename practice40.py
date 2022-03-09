#9056

from sys import stdin

while True:
    list =[]
    data = int(stdin.readline())
    if data == -1:
        break
    for num in range(1, data):
        if data % num == 0:
            list.append(num)
    if sum(list) == data:
        asd = ' + '.join(map(str, list))
        print(f"{data} = {' + '.join(map(str, list))}")
            
    else:
        print(f"{data} is NOT perfect.")
        list = []


