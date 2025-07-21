'''
    slope:m
    y-intercept: b
    value: x
    equation of line y =(m*x)+b
'''

m = float(input('Enter the value of slope:'))
b = float(input('Enter the value of y-intercept:'))
x = float(input('Enter the value of x:'))

def line_equation(m,b,x):
    y = (m*b) + x
    print (f'your slope value is:{m}, your y-intercept value is:{b}, your value of x:{x}, so slope interception is{y}')

## function calling
line_equation(m,b,x)