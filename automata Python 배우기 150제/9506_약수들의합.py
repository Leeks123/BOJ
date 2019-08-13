
#9506

t = []
#입력
while True:
    s = int(input())
    if s == -1:
        break
    t.append(s)

def check(s):
    sum=0
    li=[]
    for i in range(s):
        if s%(i+1)==0:
            sum+=(i+1)
            li.append(i+1)
    if sum==2*s:
        ret = str(s)+' = '
        for i in li:
            if i==s:
                ret=ret[:-3]
                break
            ret+=str(i)
            ret+=' + '
    else:
        ret = str(s)+' is NOT perfect.'
    return ret

for i in t:
    print(check(i))