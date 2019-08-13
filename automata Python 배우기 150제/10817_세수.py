# 10817

a, b, c = input().split(' ')
li = []
li.append(int(a))
li.append(int(b))
li.append(int(c))


def solution(li):
    li.remove(max(li))
    return max(li)


print(solution(li), end='')
