def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        temp = ""
        for i in range(s,s+l):
            temp += num[i]
        temp = int(temp)
        if temp > k:
            answer.append(temp)
    return answer