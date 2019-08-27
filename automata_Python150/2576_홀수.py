#2576

li = []
for i in range(7):
    n = int(input())
    li.append(n)

odd = []
sum = 0
for i in li:
    if i%2==1:
        odd.append(i)
        sum += i

if odd == []:
    print(-1)
else:
    print(sum)
    print(sorted(odd)[0])

