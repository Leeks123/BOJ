#2921

n = int(input())

def calcPoint(n):
    return 3*n*(n+1)/2

def pointNum(n):
    sum = 0
    for i in range(n+1):
        sum += calcPoint(i)
    return int(sum)

print(pointNum(n))