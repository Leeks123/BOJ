#1427

s = input()
li = []
for i in s:
    li.append(int(i))
li.sort(reverse=True)
for i in li:
    print(i,end='')