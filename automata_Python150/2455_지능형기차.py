#2455

li = []
for i in range(4):
    li.append(input())

people = 0
max = 0

def in_out(n):
    o,i=n.split(' ')
    i = int(i)
    o = int(o)
    global people, max
    people += i
    people -= o
    if people > max:
        max = people
    
for i in li:
    in_out(i)

print(max)