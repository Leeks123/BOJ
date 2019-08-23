#10952

li = []
while True:
    a,b=input().split(' ')
    if int(a)==0 and int(b)==0:
        break
    li.append(int(a)+int(b))

for i in li:
    print(i)