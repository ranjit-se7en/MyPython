
set1=set(range(1, 10, 2))
set2=set(range(0, 10, 2))
print(set1)
print(set2)

print(set1.union(set2))
print(set1.difference(set2))

print()

print(set1.intersection(set2))
print(set1 & set2) #same as intersection() used above


print(set1 - set2)



