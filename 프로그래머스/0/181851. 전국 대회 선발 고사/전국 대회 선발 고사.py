def solution(rank, attendance):
    arraylist = []
    for i in range(len(rank)):
        if attendance[i] == True:
            arraylist.append([rank[i],i])
            
    arraylist.sort()
    return (arraylist[0][1] * 10000 + 100 * arraylist[1][1] + arraylist [2][1])