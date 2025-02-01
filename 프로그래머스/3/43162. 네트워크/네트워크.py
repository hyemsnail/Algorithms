def solution(n, computers):
    answer = 0
    visit = [False] * n #방문횟수 저장

    def dfs(i):
        visit[i] = True
        for j in range(n):  # 전체 컴퓨터에 대해 검사
            # 만약 아직 방문하지 않았고, i와 j가 연결되어 있다면
            if not visit[j] and computers[i][j] == 1:
                dfs(j)

    for i in range(n):
        if not visit[i]:
            dfs(i)
            answer += 1
            
    return answer
