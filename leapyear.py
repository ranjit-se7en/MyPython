def is_leap(year):
    leap = False
    if (1900 <= year <=100000):
        if year % 4 ==0 and  (year % 100 !=0) or (year % 400 ==0):
            leap=True
    # Write your logic here
        else:
            leap=False
    else:
        leap=False
    return leap

year = int(input())