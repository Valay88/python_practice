'''
      *
     **
   *  *
 *    *
*******

n = 5
condition if n == 1
  return *
condition else if n == 2
    return **
else: 
for i in range(1,n+1)
for j in range(n-i)
    print(' ',end='')
for k in range(1,i+1)
    first = '*' * i 
    middle = '*' + ' '*(i-2) +'*'
    return first+[middle for i  in range of(i-2)]+first

'''
n = int(input('Enter the value of n:'))
def hollow_right_triangle(n):
        for i in range(1,n+1):
            for j in range(n-i):
                print(' ',end='')
            for j in range(i):
                if j == 0 or j == i-1 or i == n:
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
                      

## function calling
hollow_right_triangle(n)