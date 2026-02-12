# using ternary operator
order_amount = 299
print(f"Your order amount is {order_amount}. No Delivery charge") if order_amount >= 300 else print(f"Your order amount is {order_amount + 30}. 30rs delivery charge is inclusive")