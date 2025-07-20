'''
    formula = (9/5 * c) + 32
    input celcius
    f = (9/5 * c) + 32
    print(fernhite)
'''
c = int(input('Enter the temp in celcius:'))
def cel_to_fer(c):
    f = (9/5 * c) + 32
    print(f'your temprature in celcius:{c} and temprature in fernhite:{f}')

## function calling
cel_to_fer(c)