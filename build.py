def solution(num1, num2, end_num):
    lis = []
    for i in range(1,end_num):
        if i%num1 == 0 and i%num2 == 0:
            lis.append(i)
    return lis
