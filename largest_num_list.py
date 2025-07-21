'''
    l = [1,5,4,9,10]
    largest = l[0]

    for i in l:
        if i>largest:
        largest = i
    print(largest)

'''
l = [1,5,4,9,10]
def largest_num_list(l):
    m = l[0]
    for i in l:
        if i > m:
            m = i
    print('largest number in list is:',m)

largest_num_list(l)