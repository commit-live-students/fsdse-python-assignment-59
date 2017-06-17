def solution(num1, num2, end_num):
    """Enter Code Here"""
    lst = []
    i = 1
    while i in range(end_num):
        if i % num1 == 0 and i % num2 == 0:
            lst.append(i)
        i += 1
    return lst
