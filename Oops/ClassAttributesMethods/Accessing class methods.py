class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print ("Total is ",total)
    @classmethod
    def get_discount(cls):
        return cls.__discount
    @classmethod
    def set_discount(cls, discount):
        cls.__discount = discount
print(Mobile.get_discount())
