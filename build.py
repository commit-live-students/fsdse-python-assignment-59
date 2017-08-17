def solution(num1, num2, end_num):
    """Enter Code Here"""
    a = []
    c = 0
    for i in range (1, end_num):
        if i % num1 == 0 and i % num2 == 0:
            a.append(i)
    return a


'''
a = solution(2,3,20)
print a
'''
