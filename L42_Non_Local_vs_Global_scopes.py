# nonlocal keyword used to access the Enclosing scope variable in inner variable
def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After Kitchen Update:", chai_type)

update_order()

# global keyword use
chai_type = "plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Elaichi"
    kitchen()
    print("outer function:", chai_type)


front_desk()
print("Global chai type:", chai_type)