#2460

train = []
for i in range(10):
    train.append(input().split(' '))

pples = 0
max = 0

for k in train:
    pples += int(k[1])
    pples -= int(k[0])
    if max < pples:
        max = pples

print(max)