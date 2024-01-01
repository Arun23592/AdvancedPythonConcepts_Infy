class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    pass
FeaturePhone(10000,"Apple","13px").buy()
