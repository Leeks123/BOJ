#10953

t = int(input())
li = []
for i in range(t):
    li.append(input())

for i in range(len(li)):
    a,b = li[i].split(',')
    li[i]=int(a)+int(b)

for i in li:
    print(i)
