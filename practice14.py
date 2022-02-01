# 2675번


test_data = int(input())

for num in range(test_data):
    list_case = list(input())
    num = int(list_case.pop(0))
    del list_case[0]
    for case in map(lambda element : element * num, list_case):
        print(case, end = '')
    print()

    
    