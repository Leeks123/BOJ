#9325

t = int(input())
def calc(li):
    ret = li[0]
    i =1
    while i<len(li):
        ret+=li[i][0]*li[i][1]
        i+=1
    return ret

def solve():
    li = [] # [ s, (q,p), (q,p) ...]
    li.append(int(input()))
    n = int(input())
    if n>0:
        for i in range(n):
            op = []
            q,p = input().split(' ')
            q = int(q)
            p = int(p)
            op.append(q)
            op.append(p)
            li.append(op)
    return calc(li)

answer = []
for i in range(t):
    answer.append(solve())
for i in answer:
    print(i)