# 10886

n = int(input())

cute = 0
notcute = 0

for i in range(n):
    v = int(input())
    if v == 0:
        notcute += 1
    else:
        cute += 1

print('Junhee is cute!' if cute > notcute else 'Junhee is not cute!')
