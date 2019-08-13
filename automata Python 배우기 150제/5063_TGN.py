# 5063

t = int(input())
li = []
for i in range(t):
    li.append(input())


def result(s):
    r, c, e = s.split(' ')
    r = int(r)
    c = int(c)
    e = int(e)
    if r < c-e:
        return 'advertise'
    elif r == c-e:
        return 'does not matter'
    else:
        return 'do not advertise'


for i in li:
    print(result(i))
