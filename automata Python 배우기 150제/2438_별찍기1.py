#2438

def solution(n):
    i=1
    while i<=n:
        k = 0
        while k<i:
            print('*',end='')
            k+=1
        if i==n: break
        else:
            print('')
            i+=1
    
solution(5)