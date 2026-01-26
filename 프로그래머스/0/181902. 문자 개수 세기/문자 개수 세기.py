def solution(my_string):
    answer = [0] * 52
    for char in my_string:
        if char.isupper():
            index = ord(char) -65
            answer[index] +=1
        else:
            index = ord(char) - 71
            answer[index] += 1
    return answer