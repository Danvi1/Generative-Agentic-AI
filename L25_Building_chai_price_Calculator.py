chai_cup_size = input("Enter chai cup size (small/medium/large): ").lower()

if chai_cup_size == "small":
    print("The price of small chai is RS.10")
elif chai_cup_size == "medium":
    print("The price of medium chai is RS.15")
elif chai_cup_size == "large":
    print("The price of large chai is RS.20")
else:
    print("Unknown cup size. Please choose small, medium, or large.")