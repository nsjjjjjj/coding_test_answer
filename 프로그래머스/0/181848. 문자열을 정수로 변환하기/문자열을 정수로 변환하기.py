def solution(n_str):
    answer = 0
    length = len(n_str)

    for i in range(length):
        answer += int(n_str[i]) * (10 ** (length - i - 1))

    return answer