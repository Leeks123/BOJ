#5543

burger = []
juice = []
for i in range(3):
    burger.append(int(input()))
for i in range(2):
    juice.append(int(input()))

burger.sort()
juice.sort()
print(burger[0]+juice[0]-500)