#10988

str = input()

def checkPelindrom(s):
    i=0
    while i<len(s)/2:
        if s[i]==s[-1-i]:
            i+=1
            continue
        else:
            return 0
    return 1

print(checkPelindrom(str),end='')