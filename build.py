def solution(num1, num2, end_num):
    """Enter Code Here"""
    a=num1*num2
    ans = []
    i = 1
    while(i<end_num):
        if(i%a==0):
            ans.append(i)
        i=i+1
    return ans
