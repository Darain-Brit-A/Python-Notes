# dictionary  =  a collection of {key:value} pairs ordered and changeable but no duplicates

capitals = {"USA":"Washington",
            "India":"Delhi",
             "China":"Beijing",
             "Russia":"Moscow"}

print (capitals)

# THis will return the value of the key if key is not there it will return none
print(capitals.get("India"))

# update 
capitals.update({"Japan":"Tokoyo"})
capitals.update({"USA":"York"})

# pop
capitals.pop("China")
# pops the latest inserted value
capitals.popitem()

# capitals.clear() clears the entire dictornary
print(capitals)

# returns a list of all the keys this makes the variable as a object
keys = capitals.keys()

for key in capitals.keys():
    print(key)

# returns a list of the values of the dictionary as an object
values = capitals.values()

# returns a dictionary object which resembles a 2d list of a tuple
items = capitals.items()
print(items)