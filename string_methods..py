# usefull string methods

name = input("Enter your full name: ")
 
# Length of a string
print(len(name))


# finds the first occurance of a character
print(name.find(" "))

# finds the last occurance of a character 
print(name.rfind(" "))
# This returns -1 if it not there in the string

# Capitalize makes the first letter capital
print(name.capitalize())

# upper makes all the letters capital case
print(name.upper())

# lower makes all the letter lower case
print(name.lower())

# isdigit methods returns true if a string is full of digits
print(name.isdigit())

# isalpha methods returns true if it contains only alphabets
print(name.isalpha())

# count counts the number of character returns a integer
print(name.count("a"))

# replace we can replace any character in the string with a another character
print(name.replace("a",""))