def solution(num1, num2, end_num):
    """Enter Code Here"""
    lis = []
    i = 1
    while i <= end_num:
        if(i%num1 == 0 and i%num2 == 0):
            lis.append(i)
        i = i + 1

    return lis

solution(2, 3, 13)
