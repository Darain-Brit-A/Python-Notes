# for loops = excutes a block of code a fixed number of times we can iterate over a range, string, sequence

for i in range(1,11):
    print(i)

# to count in reverse
for i in reversed(range(1,11)):
    print(i)
#or
for i in range(11,1,-1):
    print(i)

# to skip steps
for i in range(1,11,2):
    print(i)

name = "Darain"
for i in name:
    print(i)

# skips a iteration - continue
for i in range(1,21):
    if i == 3:
        continue
    print(i)

# breaks out of the loop - break
for i in range(1,21):
    if i == 3:
        break
    print(i)
