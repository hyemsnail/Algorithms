def solution(n,a,b):
    answer = 0
    while a != b:
        a = a//2 + a % 2
        b = b//2 + b % 2
        answer += 1
        
    return answer
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

