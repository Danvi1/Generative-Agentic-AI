class Chai:
    def __init__(self,sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Sipping")
        
    def add_sugar(self, amount):
        print(f"Added Sugar of Amount {amount}")

my_chai =  Chai(sweetness = 3, milk_level = 4)

my_chai.sip()
my_chai.add_sugar(2)
my_chai.sip()
