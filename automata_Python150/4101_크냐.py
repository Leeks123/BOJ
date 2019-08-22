# 4101

answer = []


def bigger(a, b):
    if a > b:
        return "Yes"
    else:
        return "No"


while True:
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        break
    answer.append(bigger(a, b))

for i in answer:
    print(i)
