def solution(seoul):
    answer = ''
    for i in range(0,len(seoul)):
        if "Kim" == seoul[i]:
            answer = "김서방은 "+str(i)+"에 있다"
    return answer