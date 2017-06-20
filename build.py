def solution(num1, num2, end_num):
    list1 = [x for x in range(1, end_num) if (x % num1 == 0 and x % num2 == 0)]
    return list1
