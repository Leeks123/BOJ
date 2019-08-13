# boj 1977
import math

a = input()
b = input()


def solution(a, b):
    i = math.ceil(math.sqrt(int(a)))
    sum = 0
    while i <= math.sqrt(int(b)):
        sum += i**2
        i += 1
    if sum == 0:
        print(-1)
    else:
        print(sum)
        print(math.ceil(math.sqrt(int(a)))**2)


solution(a, b)
