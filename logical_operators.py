# logical operators evaluate multiple contions
#                   or = one condtion shd be true
#                   and = both condition shd be true 
#                   not = inverts the condtion true becomes false and vice versa


# OR
age = 19
passed = True
if age <= 18 or passed:
    print("You can enter")
else:
    print("You cant enter")

# AND

if age <= 18 and passed:
    print("You can enter")
else:
    print("You cant enter")

# NOT
if not passed:
    print("You can enter")
else:
    print("You cant enter")