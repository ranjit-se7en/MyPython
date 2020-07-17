import os
import sys
import subprocess


# class test:
#     t="This is Variable"
#     def echo(self):
#         return "This is Function"
#
# x=test()
# print(x.t)
# print(x.echo())

# class dog:
#     kind='canine'
#
#     def __init__(self, name):
#         self.name=name
#
# d=dog('Claire')
# g=dog('Chop')
#
# print("Kinds: ")
# print(d.kind, '\t',  g.kind)
#
# print("Names: ")
# print(d.name, '\t',  g.name)


class lists:
    def __init__(self):
        self.items=[]

    def additems(self, item):
        self.items.append(item)

    def addanotheritems(self, seconditem):
        self.items.append(seconditem)


a=lists()
a.additems('Mobiles')
a.addanotheritems('Charger')

print(a.items)