# 5355번



def mars_calc(num, item):
    if item == '@':
        return (num*3)
    elif item == '%':
        return (num + 5)
    elif item == '#':
        return (num - 7)


test_case = int(input())

for num in range(test_case):

    case = input().split(' ')
    num = float(case.pop(0))
    for j in case:
        num = mars_calc(num, j)
    print(f'{num:.2f}')
    
    
    


