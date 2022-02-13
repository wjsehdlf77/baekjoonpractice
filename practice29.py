#2754번


grade_list = list(input())

first_elememt = {
    'A' : 4.0,
    'B' : 3.0,
    'C' : 2.0,
    'D' : 1.0,
    'F' : 0.0
}
last_element = {
    '+' : 0.3,
    '0' : 0,
    '-' : -0.3
}
if grade_list[0] != 'F':
    grade = first_elememt[grade_list[0]] + last_element[grade_list[1]]
    print(grade)
else:
    print(first_elememt['F'])


