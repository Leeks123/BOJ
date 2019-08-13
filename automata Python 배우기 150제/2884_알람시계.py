# 2884

h, m = input().split(' ')
h = int(h)
m = int(m)
pre = 45

if m >= 45:
    m = m-pre
else:
    pre = pre-m
    h -= 1
    if h <= 0:
        h += 24
    m = 60-pre

print(str(h)+' '+str(m))
