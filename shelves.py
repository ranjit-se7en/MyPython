import shelve


#A “shelf” is a persistent, dictionary-like object.
# The difference with “dbm” databases is that the values (not the keys!) in a shelf can be
# essentially arbitrary Python objects — anything that the pickle module can handle.
# This includes most class instances, recursive data types, and objects containing lots of shared sub-objects.
# The keys are ordinary strings.


# with shelve.open("shelvewords") as file:
#     file["a"]="How"
#     file["b"]="Did"
#     file["c"]="This"
#     file["d"]="Happen"
#     for i in file:
#         print(file[i])

# text = shelve.open("shelvewords")


# while True:
#     userinput = input("Enter a letter, or type 'quit' to exit: ")
#     if userinput.casefold() == "quit":
#         break
#     else:
#         desc=text.get(userinput, "We don't have that letter,")
#         print(desc)
#
# text.close()


snacks=["eggs", "oats", "biscuits", "tea"]
lunch=["rice","soup","bread","salads"]
dinner=["chicken","eggs","bread"]

# with shelve.open("menu") as file:
#     print(snacks)
#     print(lunch)
#     print(dinner)

with shelve.open("menu", writeback=True) as file:
    snacks.append("poha")
    lunch.append("briyani")
    dinner.append("soup")

    print("Updated List")
    print("=" * 80)
    print(snacks)
    print(lunch)
    print(dinner)
    file.sync()


with shelve.open("menu") as file:

    print(dinner)
    dinner.remove("soup")
    file.sync()
    print(dinner)