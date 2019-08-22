#2439

def solution(n):
    i=1
    while i<=n:
        k = 0
        l = 0
        while l<n-i:
            print(' ',end='')
            l+=1
        while k<i:
            print('*',end='')
            k+=1 
        if i==n: break
        else:
            print('')
            i+=1
    
solution(5)