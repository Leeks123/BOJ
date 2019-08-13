#2441

def solution(n):
    i=0
    while i<=n:
        k = 0
        l = 0
        while k<i:
            print(' ',end='')
            k+=1
        while l<n-i:
            print('*',end='')
            l+=1
        
        if i==n-1: break
        else:
            print('')
            i+=1

solution(5)