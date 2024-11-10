# Task 1: Vehicle Registration System

# - Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

# - Code Example: Provide a basic structure for the Vehicle class without methods.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner    
    
    def update_owner(self, new_owner):
        self.owner = new_owner

owner1 = Vehicle(1234567, "Monster Truck", "Donovan")
owner2 = Vehicle(3987654, "Monster Truck", "Sarah")
owner3 = Vehicle(27847384, "Monster Truck", "Daniel")

owner1.update_owner("Donovan")
owner2.update_owner("Sarah")
owner3.update_owner("Daniel")

print(f"The new owner of the {owner1.type} is {owner1.owner}, and the registration number is: {owner1.registration_number}")
print(f"The new owner of the {owner2.type} is {owner2.owner}, and the registration number is: {owner2.registration_number}")
print(f"The new owner of the {owner3.type} is {owner3.owner}, and the registration number is: {owner3.registration_number}")
