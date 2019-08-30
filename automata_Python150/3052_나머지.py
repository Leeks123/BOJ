#3052

remain = []
for i in range(10):
    n = int(input())
    r = n%42
    if r in remain:
        continue
    else:
        remain.append(r)

print(len(remain))