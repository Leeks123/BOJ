#5218

t = int(input())
li = []
for i in range(t):
    li.append(input().split(' '))

def calcDist(s1,s2):
    distance = [0 for i in range(len(s1))]
    for i in range(len(s1)):
        n = ord(s2[i])-ord(s1[i])
        if n<0:
            distance[i]=n+26
        else:
            distance[i]=n
    return distance

for i in li:
    print("Distance : ",end='')
    for j in calcDist(i[0],i[1]):
        print(j,end=' ')
    print()
    