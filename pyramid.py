'''
    input=5
    i = 1
    j = (5-1) = 4     
    k= (1)                  
    i = 2
    j = (5-2) = 3
    k = (2*i-1)
            *
          * * * 
        * * * * * 
    input n
    function pyramid(n)
    for i in range(1,n+1)
        for j in range(1,n-i)
            print(' ', end= '')
        for k in range(1,2*i-1)
            print('*',end='')
'''
n = int(input('Enter the value of n:'))
def pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end='')
        for k in range(1,2*i):
            print('*',end='')
        print()
print(pyramid(n))