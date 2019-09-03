#10773

k = int(input())

li = []
for i in range(k):
    li.append(int(input()))
stack = []
for i in li:
    if i!=0:
        stack.append(i)
    else:
        stack.pop()
ret = 0
for i in stack:
    ret+=i
print(ret)