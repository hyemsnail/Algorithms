def solution(phone_number):
    answer = phone_number
    answer = list(phone_number)
    for i in range(1, len(phone_number) - 3):
        answer[-(i+4)] = "*"
    answer = "".join(answer)
    return answer