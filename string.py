import sys
import datetime
import math

# S="Hello"
# T="World"
# print (S ,"\n", T)
#
# #String Length
# print (len(S))
# print (len(T))
#
# #String Concatination
# print ( (S) + " " +  (T) )
#
#
# #Multi Line String
# print( """
#     The Sting is
#     Random
#     Test
#     """)
#
# #First Character in String
# print(S[0])
#
# #Last character in String
# print (S[-1])
#
# #Characters from 0-2 Hello
# print (S[0:2])


# l=range(1, 10)
# a=[]
# for i in l:
#     a.append(i)
# print("Before Insert")
# print(a)
#
# a.insert(10,10)
# print("After Insert")
# print(a)

# a.clear()
# print("After Clear")
# print(a)

# print("The list contains ", len(a) , 'Elements')
#
# a.reverse()
# print(a)
#
# a.sort()
# print(a)
#
# a.pop()
# print(a)

t=([1, 2, 3], [3, 2, 1])
print(t[0], "\n", t[1])
print(len(t))

d={ 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six'}

for i,j in d.items():
    print(i, j)

print(__name__)
#Print raw string without escaping
print(r"\t\n\u\r\b\c\v")

multisting="""
THis is a 
Multiple 
Line
String

"""

string="RANDOM,TEST,PLACES"
print()
print()
print()
print(multisting)
#Stepping a slice string

sliced=string.split(',')
print(sliced)

#Print 2nd letter of the word TEST in sliced String
print(sliced[1][1])

print()
test="BLAH!"
print(test * 3)

if "HA" in test:
    print("YES")
else:
    print("NO")

name="John"
age=28

print("Hello " + name + " Your age is " + str(age) + " Nice to meet you!")

print()
# above string can also be printed as follows

print("Hello {0} Your age is {1} Nice to meet you!".format(name, age))

print()

for j in range  (1, 10+1):
    print("Square of Number {:2} is {:4}, and Cube of Number {:2} is {:4}".format(j, j ** 2, j, j ** 3))