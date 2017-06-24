x = 3
y = 2
a = 90

def solution(no1, no2, up):
    lis = []
    for i in range (2, up+1):
        if ((i % no1 == 0) & (i % no2 == 0)):
            lis.append(i)
    return lis

solution(x, y, a)
#NT DOne,
