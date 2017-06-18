def solution(num1, num2, num3):
    final=[]
    for num in range(1,num3):
        if num%num1==0 and num%num2==0:
            final.append(num)
    return final
