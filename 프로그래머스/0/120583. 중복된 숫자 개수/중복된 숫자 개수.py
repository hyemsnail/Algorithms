def solution(array, n):
    answer = 0
    for number in array:
        if number == n:
            answer += 1
    return answer