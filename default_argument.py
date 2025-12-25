# default arguement = a default value for certain parameters 

def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))

# can be written as 
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))

# we can change the default also
print(net_price(500,0.01,0))


import time
# non default arguments shd be at the end not at the first
def count(end,start =0):
    for i in range(start, end):
        print(i)
        time.sleep(1)
    print("Done")

count(4)