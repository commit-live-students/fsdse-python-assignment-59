def solution(num1, num2, end_num):
    """Enter Code Here"""
    l = []
    j = 1
    while j <= end_num:
        if(j%num1 == 0 and j%num2 == 0):
            l.append(j)
        j = j + 1

    return l

solution(2, 3, 13)
