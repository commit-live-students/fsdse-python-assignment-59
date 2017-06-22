def find_lcm(num1,num2):
    greater = num1 if num1 > num2 else num2

    while True:
        if (greater % num1 == 0) and (greater % num2 == 0):
            lcm = greater
            break
        greater += 1
    return lcm

def solution(num1, num2, end_num):
    """Enter Code Here"""
    lcm = find_lcm(num1,num2)
    check = lcm
    l = []
    while(check < end_num):
        l.append(check)
        check += lcm
    return l
