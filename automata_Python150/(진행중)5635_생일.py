#5635

n = int(input())
dic = {}
for i in range(n):
    li = input().split(' ')
    dic[li[0]]=li[1:]

print(dic.items())