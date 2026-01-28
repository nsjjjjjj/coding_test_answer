def solution(arr):
    old = arr[:]
    new = arr[:]
    x = 0
    while 1:
        for i in range(len(arr)):
            if old[i] >= 50 and old[i]%2 == 0:
                old[i] //= 2
            elif old[i] < 50 and old[i]%2 == 1:
                old[i] *= 2
                old[i] += 1
        if new == old:
            return x
        new = old[:]
        x += 1