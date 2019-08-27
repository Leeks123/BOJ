#2490

t = []
for i in range(3):
    t.append(input())

def yutgame(s):
    li = s.split(' ')
    cnt = 0
    for i in li:
        if int(i)==1:
            cnt+=1
    if cnt==0:
        return 'D'
    elif cnt==1:
        return 'C'
    elif cnt==2:
        return 'B'
    elif cnt==3:
        return 'A'
    elif cnt==4:
        return 'E'

for i in t:
    print(yutgame(i))
