#11170

t = int(input())

def inZero(n):
    s = str(n)
    cnt = 0
    for i in s:
        if i=='0':
            cnt+=1
    return cnt

li=[]
for i in range(t):
    l= input().split(' ')
    li.append(l)

def ZeroInRange(a,b):
    cnt = 0
    i = a
    while i<=b:
        cnt += inZero(i)
        i+=1
    return cnt

for i in li:
    print(ZeroInRange(int(i[0]),int(i[1])))

