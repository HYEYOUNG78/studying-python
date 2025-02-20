def solution(my_string):
    answer = ''
    lst = ['a', 'e', 'i', 'o', 'u']
    for l in lst :
        if l in my_string :
            my_string = my_string.replace(l, "")
    answer = my_string
    return answer