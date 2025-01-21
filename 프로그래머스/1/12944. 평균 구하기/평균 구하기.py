def solution(arr):
    answer = 0
    total = 0
    for i in range(0, len(arr)):
        total += arr[i]
    answer = total / len(arr)
    return answer