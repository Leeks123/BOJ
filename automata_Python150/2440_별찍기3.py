#2440

def solution(n):
    i=0
    while i<=n:
        k = n-i
        while k>0:
            print('*',end='')
            k-=1
        if i==n-1: break
        else:
            print('')
            i+=1
    
solution(5)