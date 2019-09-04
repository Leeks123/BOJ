#2744

s = input()

for i in range(len(s)):
    if s[i].upper()==s[i]:
        s = s[:i]+s[i].lower()+s[i+1:]
    else:
        s = s[:i]+s[i].upper()+s[i+1:]
        
print(s)