class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

    @classmethod
    def enable_discount(cls):
        cls.set_discount(50)
    @classmethod
    def disable_discount(cls):
        cls.set_discount(0)
    @classmethod
    def get_discount(cls):
        return cls.__discount
    @classmethod
    def set_discount(cls, discount):
        cls.__discount = discount

    @staticmethod
    def calculate_tax(cust_type):
        if(cust_type=='member'):
            return 10
        else:
            return 20

print('Tax percent to be paid by members:',Mobile.calculate_tax('member'))
print('Tax percent to be paid by non-members:',Mobile.calculate_tax('non-member'))

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

Mobile.disable_discount()
mob1.purchase()
Mobile.enable_discount()
mob2.purchase()
Mobile.disable_discount()
mob3.purchase()
