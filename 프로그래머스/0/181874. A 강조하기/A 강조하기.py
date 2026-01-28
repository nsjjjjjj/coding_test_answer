def solution(myString):
    answer = list(myString)
    for i in range(len(answer)):
        if answer[i] == 'a' or answer[i] == 'A':
            answer[i] = answer[i].upper()
        else:
            answer[i] = answer[i].lower()
    return ''.join(answer)