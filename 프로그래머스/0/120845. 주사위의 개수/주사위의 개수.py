def solution(box, n):
    a = box[0] // n
    b = box[1] // n
    h = box[2] // n
    answer = a * b * h
    return answer