def solution(array, height):
    answer = 0
    for friend_h in array :
        if friend_h > height :
            answer += 1
        else :
            continue
    return answer