class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * self.discount/100
        print(self.brand, "mobile with price", self.price, "is available after discount at", total)

print("Discount percent on mobiles: ",Mobile.discount)

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000,  "Samsung")

mob1.purchase()
mob2.purchase()
mob3.purchase()

