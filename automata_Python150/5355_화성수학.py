#5335

T = int(input())

def MarsMath(s):
    expr = []
    expr = s.split(' ')
    n = float(expr[0])
    del expr[0]

    while True:
        if not expr:
            break
        if expr[0]=='@':
            n *=3
            del expr[0]
        elif expr[0]=='%':
            n +=5
            del expr[0]
        elif expr[0]=='#':
            n -=7
            del expr[0]
    return n

li = []
for i in range(T):
    s = input()
    li.append(s)

for i in li:
    print('%.2f'%MarsMath(i))