# 2754

grade = input()
ret = 0.0

if grade[0] == 'A':
    ret = 4.0
elif grade[0] == 'B':
    ret = 3.0
elif grade[0] == 'C':
    ret = 2.0
elif grade[0] == 'D':
    ret = 1.0
elif grade[0] == 'F':
    ret = 0.0

if grade[1] == '+':
    ret += 0.3
elif grade[1] == '-':
    ret -= 0.3

print(ret)
