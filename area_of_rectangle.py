'''
    area = lenth * breath
'''
lenth = float(input('Enter the lenth:'))
breath = float(input('Enter the breath:'))
def area_of_rect(lenth,breath):
    area = lenth * breath
    print (f'your lenth : {lenth}, your breath is: {breath} and area of rectangle is:{area}')

## function calling 
area_of_rect(lenth,breath)