def solution(s):
    answer = ''
    s = list(map(int, s.split(" ")))
    answer = f'{min(s)} {max(s)}'   
    return answer