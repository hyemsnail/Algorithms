def solution(n):
    answer = []
    n = str(n)
    for i in range(1,len(n)+1):
        answer.append(int(n[-i]))
    return answer