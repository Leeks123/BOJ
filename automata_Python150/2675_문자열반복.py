#2675

t = int(input())
li = []
# 문자열 입력받기
for i in range(t):
	li.append(input())
# 문자열 변경
def expandstr(s):
	n = ''
	nu,s = s.split(' ')
	for i in s:
		n+=i*int(nu)
	return n
# 문자열 출력
for i in li:
	print(expandstr(i))
