import math

def solution(n):
    if int(math.sqrt(n)) ** 2 == n :
        answer = 1
    else :
        answer = 2
    return answer