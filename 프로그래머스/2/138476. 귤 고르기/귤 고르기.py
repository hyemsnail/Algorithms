from collections import Counter
def solution(k, tangerine):
    answer = 0
    dic = Counter(tangerine)
    for i in dic.most_common():
        answer += 1
        k -= i[1]
        if k <= 0:
            break
    return answer