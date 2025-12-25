# it is a list/tuple inside a list/tuple it is used to create matrix or a table

#fruits = ["apple", "orange", "banana", "mango"]
#vegetables = ["Potato", "carrot", "leaves"]
#meat = ["chicken", "mutton", "fish"]
#basket = [fruits, vegetables, meat]

basket= [ ["apple", "orange", "banana", "mango"],
 ["Potato", "carrot", "leaves"],
["chicken", "mutton", "fish"]]

for types in basket:
    for food in types:
        print(food,end = " ")
    print()