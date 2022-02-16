# Imports
# Global variables
# Classes


class Character:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    
    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"

    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if actual_damage < 0: actual_damage = 0            
        if (self.health - actual_damage) < 0: self.health = 0
        else: self.health -= actual_damage
    
    def attack(self):
        return self.damage
        
    def get_health(self):
        return self.health

    def get_name(self):
        return self.name
        
class Monster:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    
    def __str__(self):
        return f"{self.name}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"

    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if actual_damage < 0: actual_damage = 0 
        if (self.health - actual_damage) < 0: self.health = 0
        else: self.health -= actual_damage
        print(f"{self.name} took {actual_damage} dmg")


    def attack(self):
        return self.damage
        
    def get_health(self):
        return self.health

    def get_name(self):
        return f"{self.name}"

# Functions
def hello():
    print("Hello World")
# Main code