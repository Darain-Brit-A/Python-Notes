# if lets us do some code if the condition is true if it is false it will go to the else and excute it

age  = int(input("Enter your Age: "))

if age >= 18:
    print("Major")
elif age < 0:
    print("Invalid age")
else:
    print("Minor")