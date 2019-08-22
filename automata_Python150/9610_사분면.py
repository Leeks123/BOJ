#9610

t = int(input())
Q1=0
Q2=0
Q3=0
Q4=0
Axis=0
def setQuadrant(x,y):
    global Axis, Q1, Q2, Q3, Q4
    if x==0 or y==0:
        Axis+=1
    elif x>0 and y>0:
        Q1+=1
    elif x<0 and y>0:
        Q2+=1
    elif x<0 and y<0:
        Q3+=1
    elif x>0 and y<0:
        Q4+=1

for i in range(t):
    x,y=input().split(' ')
    setQuadrant(int(x),int(y))

#출력
print('Q1: '+str(Q1))
print('Q2: '+str(Q2))
print('Q3: '+str(Q3))
print('Q4: '+str(Q4))
print('AXIS: '+str(Axis))