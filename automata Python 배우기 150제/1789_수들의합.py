#1789

s = int(input())

# 10 = 1 + 2 + 3 + 4
# 20 = (1 + )2 + 3 + 4 + 5 + 6 = 21 -1
# 30 = 1 + 2 + 3 + 4 + 5 (+ 6 )+ 7 + 8 = 36 - 6 
# 40 = 1 + 2 + 3 + 4 (+ 5 )+ 6 + 7 + 8 + 9 = 45 - 5

def AddToN(n):
    return n*(n+1)/2

def solution(s):
    i=0
    while True:
        if AddToN(i)<=s and AddToN(i+1)>s:
            return i
        i+=1

print(solution(s))
