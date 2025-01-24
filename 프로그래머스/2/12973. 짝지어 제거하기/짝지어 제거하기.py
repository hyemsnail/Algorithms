def solution(s):
    answer = 0
    stack = []  
    for i in range(len(s)):#스택이 비어있는 경우
        if len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
            
    if len(stack) == 0:
        return 1

    return answer