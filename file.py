import sys
import os

# f=open('text.txt', 'a')
# print("Before Writing File")
#
# print("After Writing File")
# f.write("\nThis is another line")
# f.close()
# #print(f.read())
#
# r=open('text.txt', 'r')
# print(r.readline())
# r.close()

#With automatically closes file descriptor

def readline(filename):
    try:
        with open(filename) as file:
            for line in file:
                print(line, end='\t')
    except OSError as err:
        print("Error Occured wile openning file {}".format(err))
        sys.exit(1)

if __name__=="__main__":
    fname=input("Please Enter the filename to read:")
    readline(fname)




