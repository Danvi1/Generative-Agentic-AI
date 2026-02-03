ingredients = ["water", "milk", "black_tea"]
print(f"initial ingredients : {ingredients}")

# adding data to list at the end
ingredients.append("sugar") 
print(f"Ingredients after appending : {ingredients}")

#  removing data from list if present
ingredients.remove("water") 
print(f"Ingredients after removing : {ingredients}")

# use of .extend()
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]
chai_ingredients.extend(spice_options)
print(f"after adding spices : {chai_ingredients}")

# use of .insert() -> takes 2 attribute
chai_ingredients.insert(2, "black_tea")
print(f"after inserting black tea at index 2 : {chai_ingredients}")