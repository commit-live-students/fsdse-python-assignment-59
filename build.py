def solution(num1, num2, end_num):
    """Enter Code Here"""
    a = []
    i = 1
    while i < end_num:
        if i%num1 == 0 and i%num2 == 0:
            a.append(i)
        else:
            pass
        i += 1
    return a
