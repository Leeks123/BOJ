# 3009

x1, y1 = input().split(' ')
x1 = int(x1)
y1 = int(y1)
x2, y2 = input().split(' ')
x2 = int(x2)
y2 = int(y2)
x3, y3 = input().split(' ')
x3 = int(x3)
y3 = int(y3)


def checkP(x1, x2, x3):
    if x1 == x2:
        return x3
    elif x1 == x3:
        return x2
    elif x2 == x3:
        return x1


print(str(checkP(x1, x2, x3))+' '+str(checkP(y1, y2, y3)))
