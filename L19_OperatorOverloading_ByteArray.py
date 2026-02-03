base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Full chai : {full_liquid_mix}")


strong_brew = ["black_tea", "water"] * 3
print(f"Strong brew : {strong_brew}")

# Use of bytearray()
raw_spice_data = bytearray(b"CINNAMON") # here b is encoding
print(f"Raw spice data : {raw_spice_data}\n")
# you can also create bytearray from list and tuple of numbers
python_ascii_list = bytearray([80, 89, 84, 72, 79, 78]) # the number range should be between 0-255 else error
python_ascii_tuple = bytearray((80, 89, 84, 72, 79, 78)) # the number range should be between 0-255 else error
print(f"Python using List : {python_ascii_list}")
print(f"Python using tuple : {python_ascii_tuple}")