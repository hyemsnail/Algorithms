from collections import deque
def solution(s):
    rotate = len(s)
    queue = deque(s)
    answer = 0
    
    for i in range(rotate):
        if i != 0:
            sym = queue.popleft()
            queue.append(sym)
            
        stack = []
        for q in queue:
            if stack:
                if stack[-1] == '[' and q == ']': 
                    stack.pop()
                elif stack[-1] == '{' and q == '}':
                    stack.pop()
                elif stack[-1] == '(' and q == ')':
                    stack.pop()
                else:
                    stack.append(q)
            else:
                stack.append(q)

        if len(stack) == 0:
            answer += 1

    return answer