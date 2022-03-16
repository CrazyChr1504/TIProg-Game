# Imports
from random import randint
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

    def get_all_atributes(self):
        return self.name, self.health, self.damage, self.armor
        
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

def save_character(characters : list()):
    """
    Takes in a character and breaks down its' attributes och saves them in a file
    Args:
        character (Character): The object that gets saved in a file
    """

    saved_characters = []
    for character in characters:
        name, health, damage, armor = character.get_all_atributes()
        save_string = f"{name}/{health}/{damage}/{armor}\n"
        saved_characters.append(save_string)

    with open("character_file.txt", "w", encoding="utf8") as f:
        for char in saved_characters:
            f.write(char)
        print(f"Your characters have been successfully saved.")

def load_characters():

    with open("character_file.txt", "r", encoding="utf8") as f:
        characters = []
        for line in f.readlines():
            attributes = line.split("/")
            this_char = Character(attributes[0],
                                  int(attributes[1]),
                                  int(attributes[2]),
                                  int(attributes[3]))
            characters.append(this_char)
        print("Characters have been loaded from your file:\n")
        return characters

# Functions
# Main code