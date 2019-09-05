#11365

sentences = []
while True:
    s = input()
    if s=="END":
        break
    sentences.append(s)

def reverse(s):
    ret = ''
    for i in range(len(s)):
        ret+=s[len(s)-1-i]
    return ret

for i in sentences:
    print(reverse(i))
