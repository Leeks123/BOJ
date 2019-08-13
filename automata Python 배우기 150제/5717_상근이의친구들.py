
#5717

li = []
while True:
    m,f=input().split(' ')
    if m=='0' and f=='0':
        break
    li.append(int(m)+int(f))

for i in li:
    print(i)