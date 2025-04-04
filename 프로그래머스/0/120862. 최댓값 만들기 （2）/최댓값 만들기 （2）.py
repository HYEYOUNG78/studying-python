def solution(numbers):
    answer = numbers[0] * numbers[1]
    for idx1, num1 in enumerate(numbers) :
        for idx2, num2 in enumerate(numbers) :
            if(idx1 == idx2) :
                continue
            elif(answer <= (num1 * num2)) :
                answer = num1 * num2
    return answer