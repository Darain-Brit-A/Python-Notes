# *args = allows us to pass mutiple non key arguements
# **kwargs  = allows us to pass mutiple keyword-arguements 
# * unpacking operator

def add(*args):
    total = 0
    print(type(args))
    for arg in args:
        total+=arg
    return total

print(add(1,2))

#def display_name(*args):
#    for arg in args:
#        print(arg, end = " ")
#display_name("Dr.","Spongebob", "Squarepants")

# kwargs 

def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
print_address(street = "123 fake street", city = "NYC", state= " NY", zip="1234")