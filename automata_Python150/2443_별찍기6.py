# 2443


def solution(n):
    for i in range(n):
        k = 0
        j = 0
        while k < i:
            print(' ', end='')
            k += 1
        while j < 2*(n-i)-1:
            print('*', end='')
            j += 1
        if(i == n-1):
            break
        print('')


solution(5)
