def solution(num1, num2, end_num):
    newlist = []
    x = 1
    while x <= end_num:
        if(x%num1 == 0 and x%num2 == 0):
            newlist.append(x)
        x = x + 1
    print newlist    
    return newlist

solution(2, 3, 13)
