#2935

a = int(input())
op = input()
b = int(input())

def answer(a,op,b):
	if op=='*':
		return a*b
	elif op=='+':
		return a+b
		
print(answer(a,op,b))