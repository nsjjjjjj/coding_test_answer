def solution(binomial):
    cul = binomial.split()
    if cul[1] == '+':
        return int(cul[0])+int(cul[2])
    elif cul[1] == '-':
        return int(cul[0])-int(cul[2])
    else:
        return int(cul[0])*int(cul[2])