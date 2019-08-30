#2592

li = []
for i in range(10):
    li.append(int(input()))

def avg(li):
    sum = 0
    for i in li:
        sum+=i
    return int(sum/len(li))

def lfreq(li):
    nu = {}
    for i in li:
        if i in nu:
            nu[i]+=1
        else:
            nu[i]=1
    
    return sorted(nu.items(),key=lambda x : x[1],reverse=True)[0][0]

print(avg(li))
print(lfreq(li))