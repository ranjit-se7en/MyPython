
shopping_list = ["milk", "bread", "eggs", "pasta", "rice"]
# for i in shopping_list:
#     if i != "pasta":
#         print("Buy item {} ".format(i))

item_to_find = "pasta"

# for i in shopping_list:
#     if i == "pasta":
#         break
#     print("But item {}".format(i))

if item_to_find in shopping_list:
        print("Item {} found at {} position".format(item_to_find, shopping_list.index(item_to_find)))
else:
    print("Item {} not found".format(item_to_find))
