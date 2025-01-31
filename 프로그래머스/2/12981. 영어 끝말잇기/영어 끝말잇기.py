def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

