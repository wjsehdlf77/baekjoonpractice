#3009번

from sys import stdin



beacon_x = []
beacon_y = []
for a in range(3):
    
    beacon1, beacon2 = map(int, stdin.readline().split())

    beacon_x.append(beacon1)
    beacon_y.append(beacon2)

for num in range(3):
    if beacon_x.count(beacon_x[num]) == 1:
        beacon1 = beacon_x[num]

    if beacon_y.count(beacon_y[num]) == 1:
        beacon2 = beacon_y[num]

print(beacon1, beacon2)



        


            


    






    