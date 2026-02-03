def solution(myString, pat):
    myString = myString.replace('A','b')
    myString = myString.replace('B','a')
    myString = myString.upper()
    return int(pat in myString)