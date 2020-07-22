Test= "do"
String="How Do You Do?"
Items=String.split(' ')

print("-" * 88)
print(String.casefold())
print("-" * 88)
print(String.upper())
print("-" * 88)
print(String.lower())
print("-" * 88)
print(String.swapcase())


#
# if Test in Items:
#     print(String)
#     print(Items)
#     print("The String '{}' is present in '{}' at '{}' Position".format(Test, Items, Items.index(Test)))
# else:
#     print("This is not what is expected")