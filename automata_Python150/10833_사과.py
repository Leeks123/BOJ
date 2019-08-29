#10833

n = int(input())
li = []

for i in range(n):
    li.append(input())

remain_apple = 0
for i in li:
    student,apples = i.split(' ')
    remain_apple += int(apples)%int(student)

print(remain_apple)