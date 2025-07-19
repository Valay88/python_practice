n = int(input('Enter the value of n:'))
def hollow_square(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['*']
    elif n == 2:
        return ['**']
    else:
        first_last = '*' * n
        middle = '*'+ ' '*(n-2)+'*'
        return [first_last]+[middle for i in range(n-2)]+[first_last]

## function calling
print(hollow_square(n))