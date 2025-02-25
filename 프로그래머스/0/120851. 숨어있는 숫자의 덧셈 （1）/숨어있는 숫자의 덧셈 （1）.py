def solution(my_string):
    answer = 0
    for i in my_string :
        try :
            if type(int(i)) == int :
                answer += int(i)
        except :
            continue
    return answer