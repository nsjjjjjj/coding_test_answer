def solution(strArr):
    count_list = [0] * 31
    
    for s in strArr:
        length = len(s)
        count_list[length] += 1
        
    return max(count_list)