#9085

t = int(input())
answer = []
for i in range(t):
    n = int(input())
    li = input().split()
    sum = 0
    for j in li:
        sum+=int(j)
    answer.append(sum)

for i in answer:
    print(i)