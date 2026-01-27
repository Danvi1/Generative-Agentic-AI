# ------ Integer ------

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total Grams of Base tea is : {total_grams}")

reamaining_tea = black_tea_grams - ginger_grams
print(f"Total Grams of Remaining tea is : {reamaining_tea}")

#  Division that gives fractional quotient (will have decimal)
milk_litres = 7
servings = 4
milk_per_servings = milk_litres / servings
print(f"Milk per seving : {milk_per_servings}")

# Division that gives without fractional quotient ( No decimal)
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Tea bag per pot {bags_per_pot}")

# Finding Leftover parts (finding reminder)
total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"leftover Cardamom pods : {leftover_pods}")

#  to the power 
base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor # output -> 2 x 2 x 2 = 8
print(f"scaled flavor strength : {powerful_flavor}")

#  readability declaration of number in python
total_tea_leaves_harvested = 1_00_00_00_000
print(f"Total leaves Harvested : {total_tea_leaves_harvested}")

# ------------ Boolean ----------------
is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling
print(f"Total actions : {total_actions}")

# Number to boolean conversion
milk_present = 0 # no milk
milk_hidden = " "
print(f"is milk present : {bool(milk_present)}")
print(f"is milk hidden : {bool(milk_hidden)}")

# Logical Operator
if( 1 and 1):
    print("true")

if (1 or 0):
    print("Yes")

if (not 0):
    print("Reversed")

# ------- Ternary operator -------
saved_money = True
is_saved = "Yes" if saved_money else "No"
print(f"{is_saved}")


# ------------- REAL NUMBERS --------------
import sys
ideal_temp = 95.5
current_temp = 95.49
print(f"Ideal Temp : {ideal_temp}")
print(f"cureent Temp : {current_temp}")
print(f"Diff Temp { ideal_temp - current_temp}")
print(sys.float_info)
