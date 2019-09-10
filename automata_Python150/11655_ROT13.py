#11655
# 65~90
# 97~122

s = input()

def ROT13(c):
    n = ord(c)
    if n>96 and n<123:
        n+=13
        if n > 122:
            n= n -123+97
    elif n>64 and n<91:
        n+=13
        if n > 90:
            n=n-91+65
    return chr(n)

answer = ''
for i in s:
    answer += ROT13(i)

print(answer)
