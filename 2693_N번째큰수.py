#2693

t = int(input())
answer = []
for i in range(t):
    li = input().split(' ')
    for i in range(len(li)):
        li[i]=int(li[i])
    li.sort(reverse=True)
    answer.append(li[2])

for i in answer:
    print(i)