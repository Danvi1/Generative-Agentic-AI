essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black_pepper"}

# set union
combined_spices = essential_spices | optional_spices
print(f"Combined spices : {combined_spices}")

# set intersection
common_spices = essential_spices & optional_spices

# set difference
only_in_essential = essential_spices - optional_spices
only_in_optional = optional_spices - essential_spices
print(f"Spices only in essential : {only_in_essential}")
print(f"Spices only in optional : {only_in_optional}")