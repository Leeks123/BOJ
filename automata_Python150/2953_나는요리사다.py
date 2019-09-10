#2953

li = []
for i in range(5):
    li.append(input().split(' '))

score = []
idx = 1
for i in li:
    total = 0
    for j in i:
        total += int(j)
    score.append((total,idx))
    idx+=1

score.sort(key=lambda x : x[0],reverse=True)
print(score[0][1],end=' ')
print(score[0][0])