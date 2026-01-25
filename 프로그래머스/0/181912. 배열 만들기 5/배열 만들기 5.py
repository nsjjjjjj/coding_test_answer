def solution(intStrs, k, s, l):
    answer = []
    for num_str in intStrs:
        temp = int(num_str[s:s+l])
    
        if temp > k:
            answer.append(temp)
    return answer
