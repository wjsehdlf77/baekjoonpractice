#5063


from sys import stdin

N = int(stdin.readline())

for n in range(N):

    r, e, c = map(int, stdin.readline().split())

    ad_profit = e - c

    no_ad = r

    if ad_profit < no_ad :
        print('do not advertise')
    elif ad_profit > no_ad:
        print('advertise')
    else:
        print('does not matter')