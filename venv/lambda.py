### even number and odd
even = lambda num: num % 2 == 0
print(even(24))
odd = lambda num: num % 2 != 0
print(odd(36))

### square, cube

sqr = lambda num:num**2
print(sqr(2))
cube =  lambda num:num**3
print(cube(2))

## square root
sqrt = lambda num: num * 3.14
print(sqrt(8))

## cubic meter to cubic foot
cu_ft = lambda num: num * 35.315
print(cu_ft(50))

### using map in lambda
"""
    We use lambda function for making one line function
    while, we are using map for iterable. 
    syntax of map is map(function name, iterable)
"""
numbers = [1,2,3,4,5]
print(list(map(lambda x:x**2,numbers)))   

### multiple parameter with map
num1 = [1,2,3]
num2 = [4,5,6]

added = list(map(lambda x,y: x+y, num1,num2))
print(added)

### small words to capital words
words = ['apple','banana','cherry']
upper_words = list(map(str.upper,words))
print(upper_words)

### filter function
"""
    A filter function is applies on the list or iterable itmes and,
    which we want a particular items from the itrable list.
"""

### Even numbers from the list
num = [1,2,3,4,5,6,7,8,9,10]
def even_num(num):
    return num % 2 == 0

sorted_even_num=list(filter(even_num,num))
print(sorted_even_num)

### find the number which is greater than 5
num = [1,2,3,4,5,6,7,8,9,10]
even_num_list = list(filter(lambda x: x>5, num))
print(even_num_list)

### using lambda and filter with two conditions
num = [1,2,3,4,5,6,7,8,9,10]
even_num_list_greater_num = list(filter(lambda x: x > 5 and x % 2 == 0,num ))
print(even_num_list_greater_num)

### using filter with dictionary to show only that data which is above 25.
people =[
    {'name':'valay','age':32},
    {'name':'sonali','age':28},
    {'name':'pranvi','age':1}
]

def age_above_25(person):
    return person['age']>25

age_above_25_output=list(filter(age_above_25,people))
print(age_above_25_output)