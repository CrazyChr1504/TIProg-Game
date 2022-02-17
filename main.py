# Imports
from resourses import Character, Monster
import random

# Global variables
turn = 1
cn = ""
 
# Classes
# Functions
def new_fight(players: list, enemies: list):
    global turn
    participants = players + enemies # Puts together the participants in one list
    random.shuffle(participants)
    

    for char in participants:
        print(f"\nTurn {turn}\n") 
        target = ""
        # Check if player or monster
        if char in players:
            target = random.choice(enemies) 
        else:
            target = random.choice(players)

        target.take_damage(char.attack())
        if target.get_health() == 0:
            print(f"{char.get_name()} has attack by {target.get_name()}.")
            print(f"{char.get_name()} has killed {target.get_name()}.")
            if(type(target) == Monster):
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        
        else:
            print(f"{char.get_name()} was attack by {target.get_name()}.")
            print(f"{char.get_name()} has {char.get_health()} hp left.")
        
        if len(players) == 0 or len(enemies) == 0:
            break
        turn += 1

def character_choice():
    global cn 
    
    cn = input("What is your hero's name?\n")
    print(f"Hello {cn} welcome to hell-mode rpg simulation.")
    print("Would you like to have a preset character stat template? Or would you like to fabricate your own character stats?")
    stat_bonus = []
    cs = int(input())

    if cs == 0:
        stat_bonus = [10,10,10]
        return stat_bonus

    elif cs == 1:
        for _ in range(3):
            bstats = []
            for i in range(4):
                roll = random.randint(1,6)
                bstats.append(roll)
            stat_bonus.append(sum(bstats))
        return stat_bonus

    else:
        print("Something went wrong, try again.")
        character_choice()

def stat_choice(stat_bonus):
    pass
    

# Main code       
def main():

    enemies = []
    monster_name = ["Gruffbarb", "Battlebubbles", "Sharpneedles", "Deathgrowl", "Vilescalp", "Smoothheart", "Stinkstink", "Meatblade"]
    players = []
    mn = 0

    character_choice()
    stat_bonus = stat_choice()
    hps = stat_bonus[0]
    atks = stat_bonus[1]
    defs = stat_bonus[2]
    p1 = Character(cn, hps, atks, defs)
    players.append(p1)
    
    random.shuffle(monster_name)
    for _ in range(random.randint(2,4)):
        enemies.append(Monster(monster_name[mn], random.randint(14,34), random.randint(1,5), random.randint(4,10)))
        mn += 1
    
    print(f"A horde of monsters has apeared.")
    for _ in range(len(enemies)):
        print(f"{enemies[_]}\n")

    
    while len(enemies) != 0 and len(players) != 0:
        new_fight(players, enemies)

    if len(enemies) == 0:
        print("The players won!")
    elif len(players) == 0:
        print("The Monsters won!")
        print("GAME OVER")
    
if __name__ == "__main__":
    main()