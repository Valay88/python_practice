'''
    1
    11
    111
    1111
    n = 5
    i = 1
    j = (1+1)
    
    input n
    function right_angle_tri(n)
    for i in range(0,n+1)
        for j in range(i+1)
            print('1',end='')
        print()
'''
n = int(input('enter the value of n:'))
def right_angle_tri(n):
    for i in range(0,n):
        for j in range(i+1):
            print(i + 1,end='')
        print()

## function calling
print(right_angle_tri(n))