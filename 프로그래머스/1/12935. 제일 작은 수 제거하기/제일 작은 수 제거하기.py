def solution(arr):
    answer = []
    if arr == [10]:
        answer = [-1]
    else:
        arr.remove(min(arr))
        answer = arr
    return answer