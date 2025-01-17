def solution(n):
    answer = 0
    pizza = 7
    if n % 7 != 0:
        answer += 1
    answer += n // 7
    return answer