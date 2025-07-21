l = [1,2,3,4,5,6]
def even_odd(l):
    even_list=[]
    odd_list = []
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
           odd_list.append(i)
    print('Even number =',even_list)
    print('odd number =',odd_list)

even_odd(l)