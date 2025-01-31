def solution(elements):
    answer = 0
    answer = set()
    l = len(elements)
    
    for i in range(0, l):
        a = elements[i]
        answer.add(a)
        for j in range(i+1, i+l):
            a += elements[j%l]
            answer.add(a)
            
    return len(answer)