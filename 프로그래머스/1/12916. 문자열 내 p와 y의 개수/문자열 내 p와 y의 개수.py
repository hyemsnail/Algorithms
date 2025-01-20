def solution(s):
    answer = True
    count_p = 0
    count_y = 0
    for i in range(0, len(s)):
        if s[i] == 'p' or s[i] == 'P':
            count_p += 1
        if s[i] == 'y' or s[i] == "Y":
            count_y += 1
    
    if count_p == count_y:
        return True
    else:
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True