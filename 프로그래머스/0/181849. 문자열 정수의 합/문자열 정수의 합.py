def solution(num_str):
    answer = 0
    for i in range(0,len(num_str)):
        answer += int(num_str[i])
    return answer