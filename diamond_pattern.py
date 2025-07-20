'''
        *
      * * *
    * * * * * 
      * * *
        *

    n = 3
    i = 1  (1,n+1) --->raw
    j = 2   (n-1) ---> space
    k = 1   (1,2*i) ---> column
    --------------> revers
    i = 3 (n,0,-1) --->row
    j = 0 (n-i) --->space
    k = 5 (2*i-1)--->column



'''
n = int(input('enter the value of n:'))
def diamond_pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end='')
        for k in range(1,2*i):
            print('*',end='')
        print()
def reverse_diamond_pyramind(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ',end='')
        for k in range(2*i-1):
            print('*',end='')
        print() 

## function calling
diamond_pyramid(n)
reverse_diamond_pyramind(n)

