def solution(array):
    answer = []
    m = max(array)
    for i in range(0, len(array)):
        if array[i] == m:
            answer.extend([m, i])
    return answer