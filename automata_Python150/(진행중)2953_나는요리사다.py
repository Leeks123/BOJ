#2953

li = []
for i in range(5):
    li.append(input())

def calc(s):
    li =s.split(' ')
    sum = 0
    for i in li:
        sum+=int(i)
    return sum

k = []
for i in li:
    n = 1
    k.append((n,calc(i)))
    n+=1

ll = sorted(k,key=lambda x:x[1],reverse=True)
print(str(ll[0][0])+' '+str(li[0][1]))
print(ll)