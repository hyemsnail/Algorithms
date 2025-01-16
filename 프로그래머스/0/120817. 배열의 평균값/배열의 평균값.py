def solution(numbers):
    answer = 0
    for number in numbers:
        answer += number
    answer = answer / len(numbers)
    return answer