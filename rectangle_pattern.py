'''
    input n(row--->lenth),m(column---->breath)
    function rectangle(n,m)
        column= '*' * n
        retunrn ['*' * m for i in range(0,n) if n>=1 and m<=100]
    function calling by (n,m) values
'''

n = int(input('enter the value of n:'))
m = int(input('enter the value of m:'))
def rectangle(n,m):
    column = '*' * n
    return ['*' * m for i in range(0,n) if n>=1 and m<=100]

## function calling
print(rectangle(n,m))