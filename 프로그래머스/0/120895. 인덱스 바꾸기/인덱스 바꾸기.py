def solution(my_string, num1, num2):
    answer = ''
    a = ''
    my_list = list(my_string)
    a = my_list[num1]
    my_list[num1] = my_list[num2]
    my_list[num2] = a
    answer = str(''.join(my_list))
    return answer