#1292

a,b = input().split(' ')
a = int(a)
b = int(b)

def makeSequence(n):
    li = []
    i = 1
    cnt = 0
    while cnt<n:
        for k in range(i):
            li.append(i)
        cnt+=i
        i+=1
    return li[:n]
sum = 0
li = sorted(makeSequence(b),reverse=True)
for i in range(b-a+1):
    sum+=li[i]

print(sum)