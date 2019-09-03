#2752

li = input().split(' ')
for i in range(3):
    li[i]=int(li[i])

li.sort()
for i in li:
    print(i,end=' ')