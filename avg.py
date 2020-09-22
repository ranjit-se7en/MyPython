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


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg=sum(student_marks[query_name]) / 3
    print("{0:.2f}".format(avg))
