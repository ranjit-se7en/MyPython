age=int(input("How old are you "))


# Simplified Chained Comparision
#Insted of if age  > 16 and age < 65:   use if 16 < age < 65:

if 16 < age < 65:

    print("You are Adult")
elif age < 16:
    print("You are Young")
else:
    print("You are Old")

