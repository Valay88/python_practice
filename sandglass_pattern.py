'''
        *****
         ***
          *
         ***
        *****
    n = 3
    i = 3 (n, 0, -1) ---> row
    j = 0   (n-i)    ---> spacing
    k = 5   (2*i-1)  ---> column
    ---------------> regular pyramid
    i = 2 (2,n+1) ---> row
    j = 1 (n-i) ---> spacing
    k = 3  (2,(2*i)-1)) ----> column
'''
n = int(input('Enter the value of n:'))
def reverse_pyramid(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ',end='')
        for k in range(2*i-1):
            print('*',end='')
        print()
def reg_pyramid(n):
    for i in range(2,n+1):
        for j in range(n-i):
            print(' ',end='')
        for k in range(1,2*i):
            print('*',end='')
        print()

reverse_pyramid(n)
reg_pyramid(n)