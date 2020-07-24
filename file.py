import sys
import os

# f=open('sample.txt', 'a')
# print("Before Writing File")
#
# print("After Writing File")
# f.write("\nThis is another line")
# f.close()
# #print(f.read())
#
# r=open('sample.txt', 'r')
# print(r.readline())
# r.close()

#With automatically closes file descriptor

# def readline(filename):
#     try:
#         with open(filename) as file:
#             for line in file:
#                 print(line, end='\t')
#     except OSError as err:
#         print("Error Occured wile openning file {}".format(err))
#         sys.exit(-1)
#
# if __name__=="__main__":
#     fname=input("Please Enter the filename to read:")
#     readline(fname)
#


# with open("sample.txt") as file:
#     lines=file.readlines()
#     # print(lines)
#     # print(file.fileno())
#     print(lines[0:5])
#
#
#
# with open("sample.txt") as file:
#     lines=file.read()
#     # print(lines)
#     # print(file.fileno())
#     print(lines[0:5])

cities=['Pune', 'Mumbai', 'Delhi', 'Kolkata', 'Banglore']

with open("cities.txt",'w') as cities_file:
    for city in cities:
        print(city, file=cities_file)

with open("cities.txt",'r') as cities_file:
    print(cities_file.readlines())



