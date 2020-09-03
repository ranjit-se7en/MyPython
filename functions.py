import random

#
# def myfunction(*args):
#     if len(args) == 0:
#         pass
#     else:
#         return args
#
#
# print(myfunction("This is Sparta"))
# print(myfunction())

with open ("randomnumers.txt", "a") as file:
    file.write(str(random.randint(1, 999999999999999999999999999999999999999)),)
    file.write("\n")
    print(random.randint(1, 99999999999999999999999999999999999999999999999), file=file)
