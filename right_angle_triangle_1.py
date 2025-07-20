'''
        *
       **
      ***
    *****
    n = 4
    i = 1  (1,n+1)
    j = 3  (n-i) 
    k = 1  (1,i+1)

'''
n=int(input('Enter the value of n:'))
def right_angle(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end='')
        for k in range(1,i+1):
            print('*',end='')
        print()

## function calling
right_angle(n)