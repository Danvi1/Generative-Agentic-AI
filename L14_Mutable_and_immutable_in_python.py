# ----------- Immutable Example ------------------

sugar_amount = "Dhanvith"
print(f"Initial sugar amount : {sugar_amount}")
print(f"ID of 2 : {id(sugar_amount)} \n")

sugar_amount2 = "Dhanvith"
print(f"ID of 2 : {id(sugar_amount2)}")

sugar_amount = 10
print(f"Second Initial sugar amount {sugar_amount}")
print(f"ID of 2 : {id(sugar_amount)}")

print(f"ID of 2 : {id(2)}")
print(f"ID of 12 : {id(12)}")
print(f"ID of 12 : {id(13)}")


# ---------- Mutable Example -----------
spice_mix = set()
print(f"Initial spice mix id : {spice_mix}")
print(f"Initial spice mix id : {id(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("Cardamom")
print(f"Initial spice mix id : {spice_mix}")
print(f"After spice mix id : {id(spice_mix)}")

