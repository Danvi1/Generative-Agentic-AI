# Tuple
masala_spices = ("cardamom", "clove", "cinnamon", "Red chilli")

spice1, spice2, spice3 = masala_spices[:3]

print(f"Main Masala spices : {spice1}, {spice2}, {spice3}")

# Tuple behind the scene
ginger_ratio , cardamom_ratio = 2, 1  #the values are like (2,1) behind the scene which is tuple
print(f"Ginger: {ginger_ratio} and Cardomom: {cardamom_ratio}")

# fliping value
ginger_ratio , cardamom_ratio  = cardamom_ratio, ginger_ratio
print(f"Ginger: {ginger_ratio} and Cardomom: {cardamom_ratio}")

# Membership testing (checking whether present in tuple)
print(f"Is ginger in masala spices ? ans -> {'ginger' in masala_spices} ")
print(f"Is ginger in masala spices ? ans -> {'cardamom' in masala_spices} ")
