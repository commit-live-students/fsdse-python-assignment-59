def solution(num1, num2, end_num):
    l = []
    for i in range (end_num) :
        if i > 1 :
            if((i % num1) == 0 and (i % num2) == 0 ) :
                l.append(i)

    return l

solution(2,3,13)
