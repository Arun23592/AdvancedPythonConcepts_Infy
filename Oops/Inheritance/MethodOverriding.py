# When the child has a method with the same name as that of the parent,
# it is said be overridden on the parent’s method. This is called as Method Overriding.
# Method overriding is also called as Polymorphism.
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside Smartphone contructor")
    def buy(self):
        print ("Buying a smartphone")

s=SmartPhone(20000, "Samsung", 13, "Android", 2)
print(s.os)
print(s.brand)



# A class can inherit from another class
#
# Inheritance improves code reuse
#
# Constructor, attributes, methods get inherited to the child class
#
# The parent has no access to the child class
#
# Private properties of a parent are not accessible directly in the child class
#
# Child class can override the methods, this is called method overriding
#
# super() is an inbuilt function which is used to invoke the parent class methods and constructor
#
# Types of Inheritance - Simple, Multi-level, Hierarchical and Multiple inheritance

