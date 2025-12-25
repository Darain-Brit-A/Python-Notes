# while loop = excutes some code while some condition is true

name = input("Enter your name: ")

while name == "":
    name = input("Enter your name")

print(f"{name}")

# infinite loops while is mostly used here

age = int(input("Enter your age:"))

while True:
    age = int(input("Enter your age:"))
    if age == 18:
        print("Exiting Loop")
        break
