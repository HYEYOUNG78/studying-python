def solution(num_list):
    answer = 0
    multi = 1
    add = 0
    for i in num_list :
        multi *= i
        add += i
    if multi < (add**2) :
        answer = 1
    elif multi > (add**2) : 
        answer = 0
    return answer