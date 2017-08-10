def solution(num1, num2, end_num):
    return [x for x in range(1, end_num) if x % num1 == 0 and  x % num2 == 0 ]
