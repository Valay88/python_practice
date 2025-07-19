'''
    input n
    for loop i in n+1: (row)
    print('*')
    for loop j in i+1: (column)
    print('*')
'''

n = int(input('Enter the size of n:'))
def generate_stars(n):
    return ['*' * n for i in range(n)]
print(generate_stars(n))
