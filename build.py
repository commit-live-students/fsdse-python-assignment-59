def solution(num1, num2, end_num):

    l = []
    i = 1
    while i < end_num:
        if i % num1 == 0 | i % num2 == 0 :
            l.append(i)
        i = i + 1
    return l

print solution(num1=2,num2=3,end_num=13)
