import os
import sys

#S=int(input("Enter a Number: "))
# print(type(S))
#
# if S < 0:
#     print("Negative Number")
#
# elif S > 0:
#     print("Positive Number")
#
# else:
#     print("Number is 0")
#
# W=range(1, 10, 1)
#
# for i in W:
#     print(i)

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'Is not Prime')
#             #break
#         else:
#             print(n, 'Is Prime ')

# for i in range (1, 11):
#     print( S, '*', i, '=' S*i  )

# while True:
#     os.system("echo This is a Test Message")
#     print("Press Ctrl + z to Stop")

#
def fibo(n):
    a = 0
    b = 1
    result = []
    while a < n:
        result.append(a)
        a, b = b,   a+b
    return result

f=fibo(99)
print(f)


# def arguments(*args,**kwargs):
#     for i in args:
#         print (i)
#     for j in kwargs:
#         print (kwargs[j])
#
# a=arguments("This is 1", "This is 2", k1="This is test 1", k2="This is test 2")
# b=arguments("This is 2", "This is 3", k1="This is test 3", k2="This is test 4")
