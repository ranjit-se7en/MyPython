import loops
import sys
import os
import math
import subprocess
from datetime import date
# print(sys.argv[0])
# f=loops.fibo(1000)
# print(f)
#
# #print(os.system("dir"))
# for i in dir(loops):
#     print(i)

# a="This is"
# b="Sparta"
#
# #print("The {a} {b} ".format(a="Nowhere", b="Someplace"))
#
# print("The value of pi is {}".format(round(math.pi), ))
#
# now=date.today()
# now.strftime("%d-%m-%y")
# print(now)

def install(package):
    os.system("Pip install {}".format(package))

try:
    import jinja2
except ImportError:
    install('jinja2')
