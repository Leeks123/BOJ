#10808

s = input()
alphabet = [0 for i in range(26)]
#n = ord(s[i])-97
for i in s:
    alphabet[ord(i)-97]+=1

for i in alphabet:
    print(i,end=' ')