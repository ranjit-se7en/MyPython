import math

print(__name__)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a // b

if __name__ == '__main__':
    print(__name__)
    try:
        a=int(input("Enter First Number"))
        b=int(input("Enter Second Number"))
        #print(locals())
        print(add(a, b))
        print(sub(a, b))
        print(mult(a, b))
        print(div(a, b))
    except ValueError as err:
        print("Error Occured '{}' Please Enter Integers Only".format(err))