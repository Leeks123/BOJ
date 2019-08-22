# 5086


def result(a, b):
    if a % b == 0:
        return 'multiple'
    elif b % a == 0:
        return 'factor'
    else:
        return 'neither'


li = []
while True:
    s = input()
    if s == '0 0':
        break
    li.append(s)

for i in li:
    s = i
    a, b = s.split(' ')
    print(result(int(a), int(b)))
