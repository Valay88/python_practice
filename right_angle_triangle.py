'''
    input n
    function right_angle_triangle(n)
        first =  ['*']
        return ['*' * (n+1) for i in range(n)]
    function calling
    print(right_angle_triangle(n)) 

'''

n = int(input('enter the value of n:'))
def right_angle_triangle(n):
    return ['*' * i for i in range(1,n+1)]
## function calling
print(right_angle_triangle(n))