#5800

K = int(input())
li = []
for i in range(K):
    l = input().split(' ')
    for j in range(len(l)):
        l[j]=int(l[j])
    li.append(l)

def analyze(li,k):
    n = li[0]
    score = li[1:]
    score.sort(reverse=True)
    max = score[0]
    min = score[len(score)-1]
    gap = 0
    for i in range(len(score)-1):
        if gap < abs(score[i+1]-score[i]):
            gap = abs(score[i+1]-score[i])
    print('Class '+str(k))
    print('Max '+str(max)+', Min '+str(min)+', Largest gap '+str(gap))

for i in range(len(li)):
    analyze(li[i],i+1)