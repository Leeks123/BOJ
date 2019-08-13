# 10869


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a//b


def mod(a, b):
    return a % b


s = input()
a, b = s.split(' ')
print(add(int(a), int(b)))
print(sub(int(a), int(b)))
print(mul(int(a), int(b)))
print(div(int(a), int(b)))
print(mod(int(a), int(b)))
