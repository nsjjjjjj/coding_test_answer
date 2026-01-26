def solution(my_string, indices):
    arr = list(my_string)
    for i in indices:
        arr[i] = ""
    return "".join(arr)