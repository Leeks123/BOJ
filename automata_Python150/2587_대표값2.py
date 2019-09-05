#2587

li = []
for i in range(5):
    li.append(int(input()))

sum =0
for i in li:
    sum+=i

li.sort()
print(sum//5)
print(li[2])
