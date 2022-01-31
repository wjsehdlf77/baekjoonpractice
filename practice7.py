# 11022문제

test_data = int(input())

for num in range(1, test_data + 1):
    A, B = map(int, input().split())
    print(f'Case #{num}: {A} + {B} = {A + B}')
