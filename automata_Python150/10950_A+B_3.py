#10950

n = int(input())
li = []
for i in range(n):
    a,b = input().split(' ')
    li.append(int(a)+int(b))

for i in li:
    print(i)