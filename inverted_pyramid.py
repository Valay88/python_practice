'''
    n = 5
    i = 1
    j = 5


    input n
    function invert_pyramid(n)
    for i in range(n,0,-1)
        for j in range(n-i)
        print(' ',end='')
        for k in range(2*i-1)
        print('*',end='')
        print()
'''
n = int(input('Enter the value of n:'))
def invert_pyramid(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ',end='')
        for k in range(2*i-1):
            print('*',end='')
        print('')

## function calling
print(invert_pyramid(n))