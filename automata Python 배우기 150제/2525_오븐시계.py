# 2525

p = input()
t = int(input())
h, m = p.split(' ')


def solution(h, m):
    if m+t >= 60:
        m = m+t
        while m>60:
            h += 1
            m = m-60
    else:
        m = m+t
    if h>=24:
        h -=24
    print('%d %d' % (h, m))


solution(int(h), int(m))
