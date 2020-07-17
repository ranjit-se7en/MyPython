import sys
# while True:
#     try:
#         x = int(input("Enter a Number: "))
#         #print(isinstance(x, int))
#         #if isinstance(x, int) == 'True':
#         print("Number is vaid")
#         exit(0)
#     except ValueError:
#         print("Please Enter a Valid Number")

# s="abc.txt"
#
# try:
#     f=open(s, 'r')
# except OSError as err:
#     print("Cannot Open file reason {} ".format(err))
# else:
#     print(f.read())
#     f.close()



def division(x, y):
    try:
        result = x / y
    except ZeroDivisionError as err:
        print("Error occured : {}".format(err))
    else:
        return result
    finally:
        print("This will always be printed")

if __name__=="__main__":
    print("The result is", division(x=int(sys.argv[1]), y=int(sys.argv[2])))
