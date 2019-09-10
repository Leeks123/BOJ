#4458

n = int(input())
strs = []
for i in range(n):
    strs.append(input())

for i in range(n):
    c = strs[i][0]
    print(c.upper()+strs[i][1:])
