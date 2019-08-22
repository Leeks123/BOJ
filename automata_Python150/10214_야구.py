#10214

t = int(input())
round = []
for i in range(9):
    round.append(input())

def check(s):
    y,k=s.split(' ')
    y=int(y)
    k=int(k)
    if y>k:
        return 'Yonsei'
    elif y<k:
        return 'Korea'
    else:
        return 'Draw'

for i in range(t):
    print(check(round[i]))

