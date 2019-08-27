#10797

d = int(input())
cars = input().split(' ')

ban_car = 0
for i in cars:
    if int(i)==d:
        ban_car+=1
    else:
        continue

print(ban_car)