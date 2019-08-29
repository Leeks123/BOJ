#2010

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

usable = 0
for i in li:
    usable += i-1

print(usable+1)