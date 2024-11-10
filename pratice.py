"""
class building:
    def __init__ (self, apartments, floors):
        self.apartments = apartments
        self.floors = floors
        
    def rent_apartment(self):
        print(f"In this apartment complex, there are {self.apartments} apartments and {self.floors} floors.")
        
        
apartment_complex1 = building(100, 5)
apartment_complex1.rent_apartment()

print()

class Lion:
    def __init__(self, color, age, weight):
        self.color = color
        self.age = age
        self.weight = weight
        
    def roar(self):
        return "ROOOAAARRRR!!!"
    
    def sleep(self):
        return "Taking a catnap."
    
    def eat(self):
        return "Zebra is on the menu!"
    
simba = Lion("brown", 1, 50)
print(f"Simba is {simba.age} years old.")
print(f"Simba's fur color is {simba.color} and weighs {simba.weight} pounds.")
print(simba.sleep())

print()
"""

import random
roll = input("Enter the word 'roll' to see if you roll high enough to escape: ").lower()

if roll.lower() == 'roll':
    outcome = random.randint(1, 10)
else:
    print("Invalid input.")
    
class alien:
    def __init__(self, name, health=10):
        self.name = name
        self.health = health
        
    def abuduction(self, outcome):
        if outcome <= 5:
            return f"You rolled {outcome} and with your last breath, you curse Zoiberg!"
        else:
            return f"You rolled {outcome} and were successfully in defeating the Zoidberg!"
        
enemy1 = alien("Zoidberg", 10)
result = enemy1.abuduction(outcome)
print(result)

