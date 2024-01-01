class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if 1000 > amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print("The balance is ", self.__wallet_balance)


c1 = Customer(100, "Arun", 30, 1000)
c1.__wallet_balance = 100000000000
c1.show_balance()
