def solution(a, b):
    answer = 0
    c, d = 0, 0
    if a > b:
        c = b
        d = a
    elif a < b:
        c = a
        d = b
    else: 
        answer = a
    for i in range(c, d+1):
        answer += i

    return answer