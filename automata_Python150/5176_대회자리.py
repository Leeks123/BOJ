#5176

k = int(input())

answer = [0 for i in range(k)]

for i in range(k):
    p,m = input().split(' ')
    seat = [0 for i in range(int(m))]
    participant = []
    for j in range(int(p)):
        participant.append(int(input()))
    for j in participant:
        if seat[j-1]==0:
            seat[j-1]=1
        else:
            answer[i]+=1

for i in answer:
    print(i)
