#function the sum of all the numbers in a variable length arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print (add(1,2,3,4,5))
print(add(1,2,3))
print(add(1,2,3,4,5,6,7,8,9))