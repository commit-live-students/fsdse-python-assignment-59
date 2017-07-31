def solution(num1, num2, end_num):
    return [i for i in range(num1*num2,end_num,num1*num2)]

print(solution(2,3,24))

help(range)
