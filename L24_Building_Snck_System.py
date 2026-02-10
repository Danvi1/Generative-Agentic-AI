snack = input("Enter your prefered snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! {snack} will be delivered to you shortly.")
else:
    print(f"Sorry, {snack} is not available at this moment.")