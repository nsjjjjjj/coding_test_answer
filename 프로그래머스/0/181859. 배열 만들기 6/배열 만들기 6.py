def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not answer:
            answer.append(arr[i])
        elif answer[-1] != arr[i]:
            answer.append(arr[i])
        else:
            answer.pop()
    return answer if answer else [-1]