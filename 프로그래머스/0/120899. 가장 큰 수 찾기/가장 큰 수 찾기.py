def solution(array):
    answer = [0,0]
    for idx, ele in enumerate(array) :
        if answer[0] < ele :
            answer[0] = ele
            answer[1] = idx
    return answer