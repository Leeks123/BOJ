#9295

t= int(input())
li = []
for i in range(t):
    li.append(input())

for i in range(t):
    a,b=li[i].split(' ')
    print('Case '+str(i+1)+': '+str(int(a)+int(b)))
    