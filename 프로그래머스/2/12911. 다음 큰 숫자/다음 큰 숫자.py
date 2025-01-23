def solution(n):
    count_1 = 0
    count_1 = bin(n)[2:].count('1')
    while True:
        n += 1
        if count_1 == bin(n)[2:].count('1'):
            break
    return n