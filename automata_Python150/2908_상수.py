#2908

a,b = input().split(' ')

def reverse(s):
    return s[2]+s[1]+s[0]

if int(reverse(a))>int(reverse(b)):
    print(int(reverse(a)))
else:
    print(int(reverse(b)))