# 2442


def solution(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        k = 0
        while k < 2*i+1:
            print('*', end='')
            k += 1
        print('')


solution(5)
