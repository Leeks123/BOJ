#2577

a = int(input())
b = int(input())
c = int(input())

def analyze(n):
    s = str(n)
    li = [0 for i in range(10)]
    for i in s:
        li[int(i)]+=1
    return li

for i in analyze(a*b*c):
    print(i)