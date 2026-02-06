chai_order = dict( type = "masala", size = "large", sugar = 2)
print(f"Chai Order : {chai_order}\n")

# Adding element to dictionary
chai_order["cooking_instuction"] = "Make chai strong" # it will add the element at the end
print(f"Adding additional Chai Order : {chai_order}\n")

#  accessing data using the key
print(f"Accessing the elemnt using the key : {chai_order["type"]}")
print(f"Accessing the elemnt using the key : {chai_order["cooking_instuction"]}\n")

# deleting an element using "del" keyword
del chai_order["sugar"]
print(f"After deleting sugar : {chai_order}\n")

# membership checking
print(f"Is sugar present in chai recipe ? : {"sugar" in chai_order}")
print(f"Is type present in chai recipe ? : {"type" in chai_order}")
print(f"Is type present in chai recipe ? : {"large" in chai_order}\n") # only check for key

# Printing all keys in dictionary using ".keys()"
print(f"Keys of chai order : {chai_order.keys()}\n")

# Printing all values in dictionary using ".values()"
print(f"Keys of chai order : {chai_order.keys()}\n")

# using .popitem() to remove last element
print(f"Popped Item Is  : {chai_order.popitem()}\n")

# using .update() to add other dictionary at the end
extra_spices = {"cardamom" : "crushed", "ginger" : "sliced"}
chai_order.update(extra_spices)
print(f"Updated Chai order : {chai_order}\n")

# Safe getting concept .get(<key>, <text_if_key_not_found>)
# print(f"Getting the value of sugar key : {chai_order['sugar']}") # This gives error because sugar key was delete and not present
print(f"Getting the value of sugar key using get : {chai_order.get("sugar", "sugar is deleted")}\n")

# Union, intersection, difference
chai_order2 = dict( type = "normal", size = "large", sugar = 3, cardamom = "non-crushed", ginger = "sliced" )
print(f"order1 : {chai_order}")
print(f"order2 : {chai_order2}")
print(f"everything in both order : {chai_order | chai_order2}") # if there is common key then second value will override first value of that key
print(f"everything in both order : {chai_order.keys() &  chai_order2.keys()}") # if there is common key then second value will override first value of that key

