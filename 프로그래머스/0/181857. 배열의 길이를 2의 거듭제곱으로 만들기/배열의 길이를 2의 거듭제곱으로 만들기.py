def solution(arr):
    length = len(arr)
    a = 1
    while length > a:
        a *= 2
    a -= length
    for i in range(a):
        arr.append(0)
    return arr