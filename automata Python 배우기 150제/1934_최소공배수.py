#1934

t = int(input())

#데이터 입력
li = []
for i in range(t):
    li.append(input())

# A = GCD*a
# B = GCD*b
# LCM = GCD*a*b
#최소공약수
def getGCD(n,m):
    a = m if m>n else n
    b = n if m>n else m
    r = a%b
    if r==0:
        return b
    else:
        return getGCD(b,r)
#최대공배수
def getLCM(A,B):
    gcd = getGCD(A,B)
    a = A//gcd
    b = B//gcd
    return a*b*gcd

for i in li:
    a,b=i.split(' ')
    print(getLCM(int(a),int(b)))

    # 36 24 -> 24 12 