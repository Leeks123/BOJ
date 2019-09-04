#3058

t = int(input())
li = []
for i in range(t):
    l = input().split(' ')
    for i in range(len(l)):
        l[i] = int(l[i])
    li.append(l)

def analyze(li):
    li.sort()
    sum = 0
    smallest = 0
    for i in li:
        if(i%2==0):
            sum+=i
    for i in li:
        if(i%2==0):
            smallest=i
            break
    return str(smallest)+' '+str(sum)

for i in li:
    print(analyze(i))
