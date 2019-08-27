#2475

li = input().split()
sum=0
for i in li:
    sum+=int(i)*int(i)

print(sum%10)