#5054

testcase = int(input())
store = 0
position = []
answer = []
def shortestWay(store,position):

    ret = 0
    for i in range(store-1):
        ret += position[i+1]-position[i]
    return ret*2
    

for i in range(testcase):
    store = int(input())
    li = input().split(' ')
    for j in li:
        position.append(int(j))
    position.sort()
    answer.append(shortestWay(store,position))
    store = 0
    position = []

for i in answer:
    print(i)