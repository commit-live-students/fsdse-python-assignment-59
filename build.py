def solution(num1, num2, end_num):
    """Enter Code Here"""
    if num1 > 0 and num2 > 0 and end_num > 0:
        div_by_two = [div_by_two for div_by_two in range(1,end_num+1) if div_by_two%num1==0 and div_by_two%num2==0]

    return div_by_two
