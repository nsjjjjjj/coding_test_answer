def solution(my_string, s, e):
    front = my_string[:s]
    middle = my_string[s:e+1][::-1]
    back = my_string[e+1:]
    answer =front+middle+back
    return answer