import shelve

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