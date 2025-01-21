def solution(sizes):
    answer = 0
    w = []
    h = []
    for i in range(0, len(sizes)):
        w.append(max(sizes[i]))
        h.append(min(sizes[i]))
    answer = max(w) * max(h)
    return answer