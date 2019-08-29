#10178

t = int(input())
li = []
for i in range(t):
    li.append(input())

def solve(candy,sibling):
    print("You get "+str(candy//sibling)+" piece(s) and your dad gets "+str(candy%sibling)+" piece(s).")

for i in li:
    candy,sibling = i.split(' ')
    candy = int(candy)
    sibling = int(sibling)
    solve(candy,sibling)

