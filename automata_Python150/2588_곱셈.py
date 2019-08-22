#2588

n1 = int(input())
n2 = int(input())

n3 = n1*(n2%10)
n2 = n2//10
n4 = n1*(n2%10)
n2 = n2//10
n5 = n1*(n2%10)

n6 = n3+10*n4+100*n5

print(n3)
print(n4)
print(n5)
print(n6)
