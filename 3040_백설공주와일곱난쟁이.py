#3040

li = []
for i in range(9):
    li.append(int(input()))
li.sort()
sum = 0
for i in li:
    sum+=i
r = sum-100

i=0
while i<len(li):
    j=i+1
    while j<len(li):
        if li[i]+li[j]==r:
            del li[i]
            del li[j-1]
            break
        j+=1
    i+=1

for i in li:
    print(i)