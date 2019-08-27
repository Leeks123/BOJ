#2056

n = int(input())
check = input().split(' ')

def score(check):
    ret = 0
    tmp = 1
    for i in check:
        if int(i)==1:
            ret+=tmp
            tmp+=1
        elif int(i)==0:
            tmp=1
    return ret

print(score(check))