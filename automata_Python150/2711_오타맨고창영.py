#2711

t = int(input())
li = []
for i in range(t):
    li.append(input().split(' '))

def removeSpell(n,s):
    return s[0:n-1]+s[n:]

for i in li:
    print(removeSpell(int(i[0]),i[1]))