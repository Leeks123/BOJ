#10818

n = int(input())
li = input().split(' ')
ll = []
for i in li:
    ll.append(int(i))
ll.sort()
print(str(ll[0])+' '+str(ll[4]))