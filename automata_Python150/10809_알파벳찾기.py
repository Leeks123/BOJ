#10809

s = input()
alphabet = [-1 for i in range(26)]
# a = 97 --- 0
# ord(x) 문자를 아스키
# chr(x) 아스키를 문자
for i in range(len(s)):
    n = ord(s[i])-97
    if alphabet[n]==-1:
        alphabet[n]=i

for i in alphabet:
    print(i,end=' ')
