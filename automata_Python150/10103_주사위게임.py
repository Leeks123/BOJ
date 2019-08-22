#10103

#데이터 입력
t = int(input())
li = []
for i in range(t):
    li.append(input())

CY = 100
SD = 100

def diceGame(s):
    cy,sd = s.split(' ')
    cy = int(cy)
    sd = int(sd)
    global CY
    global SD
    if cy>sd:
        SD = SD-cy
    elif cy<sd:
        CY = CY-sd

for i in li:
    diceGame(i)

print(CY)
print(SD)