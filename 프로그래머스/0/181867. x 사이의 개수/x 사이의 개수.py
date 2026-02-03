def solution(myString):
    splitStr = myString.split('x')
    answer = []
    for s in splitStr:
        answer.append(len(s))
    return answer