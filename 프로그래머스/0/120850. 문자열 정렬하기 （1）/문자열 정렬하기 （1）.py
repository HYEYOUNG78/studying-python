def solution(my_string):
    answer = []
    my_list = list(my_string)
    for i in my_list :
        try :
            answer.append(int(i))
        except :
            continue
    answer.sort()
    return answer