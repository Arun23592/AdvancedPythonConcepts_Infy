class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address
    def view_details(self):
        print (self.name, self.age, self.phone_no)
        print (self.address.door_no, self.address.street, self.address.pincode)
    def update_details(self, add):
        self.address = add
class Address:
    def __init__(self, door_no, street, pincode):
        self.door_no = door_no
        self.street = street
        self.pincode = pincode
    def update_address(self):
        pass
add1=Address(123, "5th Lane", 56001)
add2=Address(567, "6th Lane", 82006)
cus1=Customer("Jack", 24, 1234, add1)
cus1.view_details()
cus1.update_details(add2)
cus1.view_details()
