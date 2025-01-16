def solution(array, height):
    answer = 0
    for number in array:
        if number > height:
            answer += 1
    return answer