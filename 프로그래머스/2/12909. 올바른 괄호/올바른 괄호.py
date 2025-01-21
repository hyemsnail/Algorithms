def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif stack == []:
            return False
        elif i == ")":
            stack.pop()
    return len(stack) == 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

