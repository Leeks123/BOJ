#9086

t = int(input())
li = []
for i in range(t):
    li.append(input())

for i in li:
    print(i[0],end='')
    print(i[len(i)-1])