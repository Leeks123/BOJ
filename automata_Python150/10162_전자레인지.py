# 10162

n = int(input())


def solution(n):
    a = 0  # 300
    b = 0  # 60
    c = 0  # 10
    if n >= 300:
        a = n//300
        n = n % 300
    if n >= 60:
        b = n//60
        n = n % 60
    if n >= 10:
        c = n//10
    else:
        return -1
    return str(a)+' '+str(b)+' '+str(c)


print(solution(n), end='')
