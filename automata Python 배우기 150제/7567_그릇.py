# 7567

plate = input()

height = 10
before = plate[0]

for i in range(1, len(plate)):
    if before == plate[i]:
        height += 5
    else:
        height += 10
        before = plate[i]

print(height)
