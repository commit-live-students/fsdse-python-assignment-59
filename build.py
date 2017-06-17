def solution(num1, num2, end_num):
    ls = []
    i=1
    nos = range(1,end_num+1)
    while(i!=len(nos)):
        if (i%num1==0)and(i%num2==0):
            ls.append(i)
        i=i+1
    print ls
    return ls
#This does use a loop, but NOT a for-loop.
solution(2,3,13)
