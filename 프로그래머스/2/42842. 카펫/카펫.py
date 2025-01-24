def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for height in range(1,int(total**0.5) + 1):
            if total % height == 0:
                width = total // height  # 가로 길이 계산
            if (width - 2) * (height - 2) == yellow:  # 노란색 타일 조건 확인
                return [width, height]  # 가로와 세로 반환
