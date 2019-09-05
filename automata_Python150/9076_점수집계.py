#9076

t = int(input())
li = []
for i in range(t):
    l=input().split(' ')
    for j in range(5):
        l[j] = int(l[j])
    l.sort()
    li.append(l)

for i in range(len(li)):
    sum = 0
    if li[i][3]-li[i][1]>=4:
        li[i] = 'KIN'
    else:
        for k in li[i]:
            sum+=k
        sum = sum-li[i][0]-li[i][4]
        li[i] = sum

for i in li:
    print(i)


