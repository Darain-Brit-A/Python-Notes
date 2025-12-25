import random

# random integer from 1 to 6
number = random.randint(1,6)

# random float number returns from 0 to 1
number = random.random()

# chooses anything in the list
options = ("Rock","paper","scissors")
print(random.choice(options))
print(number)

# shuffles the entire list
cards = ["1","2","3","4"]
random.shuffle(cards)
print(cards)