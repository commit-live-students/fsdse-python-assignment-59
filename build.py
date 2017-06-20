def solution(num1, num2, end_num):
    """Enter Code Here"""
    if num1 > 0 and num2 > 0 and end_num > 0:
        x = [x for x in range(1,end_num+1) if x%num1==0 and x%num2==0]

    return x

#solution(2, 3, 13)
#Input [6,12]
