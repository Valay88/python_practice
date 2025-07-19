'''
    input n 
    function inverter_right_angle_triangle(n)
        return '*' * i (loop n,-1)
'''
n= int(input('Enter the value of n:'))
def inverted_right_angle_triangle(n):
    return ['*' * (i-1) for i in range(n,1,-1)]

print(inverted_right_angle_triangle(n))