#2480

a,b,c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)

def big(a,b,c):
    if a<b: 
        return c if b<c else b
    else:
        return c if a<c else a

def solution(a,b,c):
    if a==b and b==c:
        return 10000+a*1000
    elif a!=b and a!=c and b!=c:
        return big(a,b,c)*100
    else:
        return (a if a==b else b)*100+1000

print(solution(a,b,c))