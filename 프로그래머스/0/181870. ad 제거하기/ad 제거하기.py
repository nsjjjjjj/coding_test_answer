def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        f = strArr[i].find('ad')
        if f == -1:
            answer.append(strArr[i])
    return answer