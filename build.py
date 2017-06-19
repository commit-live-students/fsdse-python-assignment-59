def solution(num1, num2, end_num):
    """Enter Code Here"""
    test = list(range(1,end_num))
    result = []
    result = filter(lambda x: x%num1==0 and x%num2 == 0, test)
    return result
