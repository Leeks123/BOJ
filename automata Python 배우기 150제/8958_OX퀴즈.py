
#8958

t = int(input())
answer = []

def score(s):
    ret=0
    tmp=0
    for i in s:
        if i=='O':
            tmp+=1
            ret+=tmp
        else:
            tmp=0
    return ret

for i in range(t):
    answer.append(score(input()))

for i in answer:
    print(i)