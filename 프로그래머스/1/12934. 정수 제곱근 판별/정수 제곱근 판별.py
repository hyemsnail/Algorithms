def solution(n):
    answer = 0
    number = n ** (1/2)
    if number == int(number):
        answer = (number+1) ** 2
    else:
        answer = -1
    return answer