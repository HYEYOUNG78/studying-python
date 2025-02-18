def solution(sides):
    answer = 0
    sides.sort()
    max_length = sides[-1]
    sum_length = sides[0] + sides[1]
    if max_length < sum_length :
        answer = 1
    elif max_length >= sum_length :
        answer = 2
    return answer