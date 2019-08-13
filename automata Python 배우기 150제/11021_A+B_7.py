#11021

n = int(input())

def inputdata(n):
    answer = []
    for i in range(n):
        a,b=input().split()
        a=int(a)
        b=int(b)
        answer.append(a+b)
    return answer

def answer(li):
    k = 1
    for i in li:
        print('Case #%d: '%k,end='')
        print(i)
        k+=1

answer(inputdata(n))
