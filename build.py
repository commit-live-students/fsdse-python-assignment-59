def solution(num1, num2, end_num):
    """Enter Code Here"""
    lis1 = [x for x in range(1,end_num+1) if x % num1==0 and x%num2==0 ]
    return lis1
