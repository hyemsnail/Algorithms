def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        l1 = [] # 한 행 곱셈 결과 저장
        for j in range(len(arr2[0])):
            a = 0
            for k in range(len(arr2)):
                a += arr1[i][k] * arr2[k][j]
            l1.append(a)
        answer.append(l1)

    return answer