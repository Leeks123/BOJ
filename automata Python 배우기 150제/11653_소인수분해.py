#11653

n = int(input())



def solution(n):
    tmp = n
    pn = []
    i=2
    while i<=tmp:
        if tmp==1:
            pn.append(i)
            break
        if tmp%i==0:
            pn.append(i)
            tmp = tmp//i
            #print(tmp)
        else:
            i+=1
    return pn
        
for i in solution(n):
    print(i)