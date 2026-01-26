def solution(arr):
    answer = []
    first = -1
    last = -1
    for i in range(len(arr)):
        if first == -1 and arr[i] == 2:
            first = i
        elif first != -1 and arr[i] == 2:
            last = i+1
    if first == -1:
        return [-1]
    elif last == -1:
        return [2]
    else:
        return arr[first:last]
