def solution(s):
    listS = s.split(' ')
    #리스트의 크기만큼 각 단어에 첫글자 대문자화
    for i in range(len(listS)):
        listS[i] = listS[i].capitalize()
    answer = ' '.join(listS)    
    return answer