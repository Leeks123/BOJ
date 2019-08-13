# 11098


def inputdata(n):
    i = 0
    dic = {}
    while i < n:
        s = input('문자열 : ')
        x,y = s.split(' ')
        dic[x] = y
        i += 1
    sortkey = sorted(dic.keys(),reverse=True)
    return dic[sortkey[0]]

def solution(n):
    i = 0
    li = []
    while i<n:
        li.append(inputdata(int(input('선수 수:'))))
        i+=1
    for l in li:
        print(l)

a = int(input('구단 수 : '))
solution(a)

#데이터 입력을 분할해서가 아니라 전체입력받는 방식으로 수정해야