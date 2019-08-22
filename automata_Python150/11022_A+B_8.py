#11022

n = int(input())


def solution(n):
    n1=[]
    n2=[]
    for i in range(n):
        a,b=input().split()
        a=int(a)
        b=int(b)
        n1.append(a)
        n2.append(b)
    k = 0
    for i in range(n):
        print('Case #%d: %d + %d = %d'%(k+1,n1[k],n2[k],n1[k]+n2[k]))
        k+=1 

solution(n)