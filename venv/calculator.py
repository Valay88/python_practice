def add(*args):
    total = 0
    for i in args:
        total = i + i
    return total

def mul(*args):
    total = 0
    for i in args:
        total = i*i
    return total

def sub(*args):
    total = 0
    for i in args:
        total = i - i
    return total

def div(*args):
    total = 0
    for i in args:
        total = i / i
    return total
print(add(1,2,3,4))
print(mul(1,2,3,4))
print(sub(100,80,20))
print(div(100,50))        
