l = [1,2,2,3,4,6,6,2,1,9]
k = []
def remove_duplicate(l,k):
    for i in l:
        if i not in  k:
            k.append(i)
    print(k)

remove_duplicate(l,k)