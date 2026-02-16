# Using match-case (switch case in python)

seat_type = input("Enter your seat type (Luxury/Ac/Sleeper/General): ").lower()

match seat_type:
    case "luxury":
        print("Luxury : Premium seats and facility")
    case "ac":
        print("AC : Comfortable seats with AC facility")
    case "sleeper":
        print("Sleeper : Reclining seats for a good night's sleep")
    case "general":
        print("General : Basic seats with no frills")
    case _:
        print("Invalid seat type selected.")
