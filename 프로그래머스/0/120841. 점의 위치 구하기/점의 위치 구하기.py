def solution(dot):
    
    if dot[0] > 0 :
        if dot[1] > 0 :
            answer = 1
        elif dot[1] < 0 :
            answer = 4
    elif dot[0] < 0 :
        if dot[1] > 0 :
            answer = 2
        elif dot[1] < 0 :
            answer = 3
        
    return answer