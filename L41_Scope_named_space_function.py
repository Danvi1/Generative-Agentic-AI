# Scopes
def serve_chai():
    chai_type = "Masala" #Local scope
    print(f"Inside function {chai_type}") #refers to local scope variable

chai_type = "Lemon" #global scope
serve_chai()
print(f"Outside the function {chai_type}") #refers to global scope variable

#Nested Function
def chai_counter():
    chai_order = "lemon" #Enclosing Scope
    def print_order(): 
        chai_order = "Ginger"
        print(f"Inner : {chai_order}")
    print_order()
    print(f"Outer function: {chai_order}")

chai_order = "Tulsi" #Global Scope
chai_counter()
print("Global scope:", chai_order)
