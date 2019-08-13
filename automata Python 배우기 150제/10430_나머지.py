#10430

s = input()
a,b,c=s.split(' ')

print((int(a)+int(b))%int(c))
print((int(a)%int(c)+int(b)%int(c))%int(c))
print((int(a)*int(b))%int(c))
print(((int(a)%int(c))*(int(b)%int(c)))%int(c))