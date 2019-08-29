#10984

semester = int(input())

def input_grade():
    n = int(input())
    li = []
    for i in range(n):
        li.append(input())
    return li

def calc_gpa(li):
    subjectNum =0
    sum = 0
    for i in li:
        c,g=i.split(' ')
        c = int(c)
        g = float(g)
        sum += c*g
        subjectNum += c
    return str(subjectNum)+' '+str(round(sum/subjectNum,1))

answer = []
for i in range(semester):
    answer.append(calc_gpa(input_grade()))

for i in answer:
    print(i)