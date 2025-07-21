'''
    maximum capcity of entering lift at a time = 3
    round = n (number of people)/capacity
'''

n = int(input('Enter the total person:'))
def number_of_round(n):
    capacity = 3
    round = int(round(n / capacity))
    print(f'Total number of people is:{n} where the lift capacity is:{capacity} hence no of round in lift is:{round}')

##function calling
number_of_round(n)