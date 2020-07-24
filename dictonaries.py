fruits={"apple" : "sweet", "orange" : "sour", "banana" : "sweet"}
vegetables={"potato" : "brown", "tomato" : "red", "onion" : "round"}

print(fruits)
print(vegetables)

combined=(fruits,vegetables)

print(combined)

fruits["grape"]="small"
print(fruits)
print(fruits["orange"])

del fruits["grape"]
print(fruits)


# if "grape" in fruits:
#     print("Present")
# else:
#     print("Not Present")


# value=input("Enter a fruit name: ")
# desc=fruits.get(value, "Does not exist") #Default value if key does not exist in dictonary
# print(desc)

vegetables.update(fruits)

newfruits=fruits.copy()

print(vegetables)
print()
print(newfruits)