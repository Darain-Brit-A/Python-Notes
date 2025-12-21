# formart specifiers  = {value:flags} format a value based on what flags are inserted

price1 = 3.1324
price2 = -23.456
price3 = 3343454.67

# prints the number of decimals after the point
print(f"Price 1  is ${price1: .2f}")

# has only the number of spaces to display
print(f"Price 1  is ${price1:5}")

# if we want 0 padded like 0009
print(f"Price 1  is ${price1:05}")

# if we want left justified numbers
print(f"Price 1  is ${price1:>5}")

# if we want right justified (default)
print(f"Price 1  is ${price1:<5}")

# center aligned
print(f"Price 1  is ${price1:^10}")

# to want + sign
print(f"Price 1  is ${price1:+}")
# or if want space
print(f"Price 1  is ${price1:}")

# comma in numbers
print(f"Price 3  is ${price3:,}")

#can have multiple also
print(f"Price 3  is ${price3:+,.2f}")








