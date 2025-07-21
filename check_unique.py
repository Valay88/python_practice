'''

'''
l = [1,2,3,4,5,6,7,8,7,8]


def unique_num(l):
    if len(l) == len(set(l)):
        print('this is unique list')
    else:
        print('this is not a unique list')
unique_num(l)