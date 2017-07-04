def solution(num1, num2, end_num):
    """Enter Code Here"""
    mylist = []
    for i in range(1,end_num):
        if i%num1==0 and i%num2==0:
            mylist.append(i)

    return mylist
