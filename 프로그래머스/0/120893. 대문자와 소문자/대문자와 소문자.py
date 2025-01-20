def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper() == True:
            i = i.lower()
            answer += i
        else:
            i = i.upper()
            answer += i
    return answer