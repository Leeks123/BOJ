#10807

n = int(input())
li=input().split(' ')
v = int(input())
cnt = 0
for i in li:
    if v == int(i):
        cnt+=1

print(cnt)
