import math
import sys


def avg(*args):
    sum=0
    lenth = len(args)
    for i in args:
        sum=sum+i
    result=(sum/lenth)

    print(sum)
    print(lenth)
    print(result.__round__(2))
    print("*" * 100)


avg(26, 31, 47, 54, 63, 12, 73, 3, 5)
avg(12, 32, 56, 34)