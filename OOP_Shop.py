# Parent class
class Customer:
    # customer details
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # customer details printer    
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

# Child class
class Shop(Customer):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.total_purchase = 0
        self.product_list = []
        self.price_list = []

    # total purchase  
    def product(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
        
        self.product_list.append(product_name)
        self.price_list.append(str(product_price))

        self.total_purchase = self.total_purchase + self.product_price
        
        
    # reciept        
    def show_reciept(self):
        print(f"Total purchase amount : ${self.total_purchase}")
        i = 0
        while i < len(self.product_list):
            print(f"{self.product_list[i]}: ${self.price_list[i]}")
            i += 1


# Luca's details
Luca = Shop('Luca', 23, 'Male')
# Luca.show_details()

# Luca's purchases
Luca.product('Potato', 0.90)
Luca.product('Apple', 2.50)
Luca.product('Grapes', 3.00)
Luca.product('Onion', 0.65)
Luca.product('Tomato', 1.50)

Luca.show_reciept()
