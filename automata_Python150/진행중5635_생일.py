#5635

n = int(raw_input())
dic = {}
for i in range(n):
    li = raw_input().split(' ')
    dic[li[0]]=li[1:]

print(dic.items())