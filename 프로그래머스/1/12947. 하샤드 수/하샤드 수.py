def solution(x):
    answer = True
    total = 0
    x1= list(str(x))
    for i in range(0,len(x1)):
        total += int(x1[i])
    
    if x % total != 0:
        answer = False
    return answer