import heapq as hp

def solution(operations):
    q = []
    for i in operations:
        ins, num = i.strip().split()
        num = int(num)
        
        if ins == 'I':
            hp.heappush(q, num)  # 최소 힙에 삽입
        elif ins == 'D' and q:  # 큐가 비어 있지 않을 때만 실행
            if num == -1:
                hp.heappop(q)  # 최소값 제거
            elif num == 1:
                # 최대값을 찾아 제거해야 함
                q.remove(max(q))
                hp.heapify(q)  # 힙 속성 유지

    return [max(q), min(q)] if q else [0, 0]
