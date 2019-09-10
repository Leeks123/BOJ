#11721

s = input()
cnt = 0
for i in range(len(s)):
    #global cnt
    if cnt==10:
        print()
        cnt=0
    print(s[i],end='')
    cnt+=1