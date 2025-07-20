'''
    1
    12
    345
    6789
    n = 4
    num = 1 --->inside function
    i = 1  (1,n)---->rows
    j = 2   (i+1)---->column
    ---> num = num + 1  
'''
n = int(input('Enter the value of n:'))
def floyds(n):
    num = 1
    for i in range(0,n):
        for j in range(i+1):
            print(num,end='')
            num = num+1
        print()

## function calling
print(floyds(n))