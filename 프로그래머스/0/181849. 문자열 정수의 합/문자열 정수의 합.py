def solution(num_str):
    text_list = list(num_str)
    answer = 0
    for i in text_list:
        answer += int(i)
        
    return answer