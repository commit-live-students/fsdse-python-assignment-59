def lcm(x,y):
    if x > y :
        g=x
    else:
        g=y
    while(True):
        if((g%x==0) and (g%y==0)):
            lcm=g
            break
        g+=1
    return lcm

def solution(num1, num2, end_num):
    l=lcm(num1,num2)
    return [i for i in range(num1*num2,end_num,l)]

print(solution(2,3,24))

help(range)
