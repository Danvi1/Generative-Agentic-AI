#Task3 Hinding Implementation Details

def get_input():
    print("Getting User Data")

def validate_input():
    print("validating Data")

def save_to_db():
    print("Saving to Database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User Added to the DB")

register_user()



#Task 4 Improving Readability
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

def bill_total(cups, price):
    total_bill = calculate_bill(cups, price)
    print(f"Total bill for {cups} cups is: {total_bill}")

bill_total(5, 20)
bill_total(20, 15)

print("Total bill is:",calculate_bill(60, 12)) #after colon there will be additional space



# Task5 Improving Traceability
def add_vat(price, vat_rate):
    return price + price * vat_rate / 100

orders = [100, 150, 200]

for price in orders:
    vat_rate = 10 #in percentage
    print(f"Original Price: {price}, Total price after 10% VAT is: {add_vat(price, vat_rate)}")