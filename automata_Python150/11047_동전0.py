#11047

n,k = input().split(' ')
n = int(n)
k = int(k)
coins = []
for i in range(n):
    coins.append(int(input()))

def check(k,answer):
    idx = 0
    for i in range(len(coins)):
        if k < coins[i]:
            idx = i
            break
    answer += k // coins[idx-1]
    k = k % coins[idx-1]
    if k == 0:
        return answer
    else:
        return check(k,answer)

print(check(k,0))