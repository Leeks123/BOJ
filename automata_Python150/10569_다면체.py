#10569

t = int(input())
li = []
for i in range(t):
    li.append(input())

def phase(v,e):
    return 2-v+e

for i in li:
    v,e=i.split(' ')
    print(phase(int(v),int(e)))