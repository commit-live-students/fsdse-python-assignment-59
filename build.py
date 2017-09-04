def solution(num1, num2, end_num):
    d = []
    for i in range(1,end_num):
        if(i%num1 == 0 and i%num2 == 0):
            d.append(i)
    return d

print solution(3,6,27)    
