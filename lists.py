# collection = single variable used to store multiple values'
# Lists = [] ordered and can be changed duplicates allowed


# List
fruits = ["apple", "banana", "orange", "mango"]
print(fruits[::-1])

# printing using for loop
for fruit in fruits:
    print(fruit)

# length of a list
print(len(fruits))

fruits[0] = "apples"
print(fruits[0])

# append
fruits.append("pineapple")
print(fruits[:])

# remove 
fruits.remove("apples")
print(fruits)

# insert 
fruits.insert(1,"grape")
print(fruits)

# sort
fruits.sort()
print(fruits)

# reverse
fruits.reverse()
print(fruits)

# index
print(fruits.index("banana"))

# clear
# fruits.clear()

# count
print(fruits.count("banana"))