# Imports
from resourses import Character, Monster, save_character, load_characters
from time import sleep
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
            sleep(1)
        
        else:
            print(f"{char.get_name()} was attack by {target.get_name()}.")
            print(f"{char.get_name()} has {char.get_health()} hp left.")
            sleep(1)

        if len(players) == 0 or len(enemies) == 0:
            break
        turn += 1

def character_choice():
    global cn 
    
    cn = input("\nWhat is your hero's name?\n")
    print(f"\nHello {cn} welcome to hell-mode rpg simulation.")
    print("Would you like to have a preset character stat template? Or would you like to fabricate your own character stats? (y/n)")
    stat_bonus = []
    cs = input()

    if cs.lower() == "n":
        stat_bonus = [10,10,10]
        return stat_bonus

    elif cs.lower() == "y":
        for _ in range(3):
            bstats = []
            for i in range(4):
                roll = random.randint(1,6)
                bstats.append(roll)
            stat_bonus.append(sum(bstats))
        return stat_bonus

    else:
        print("\nSomething went wrong, try again.")
        character_choice()

def stat_choice(stat_bonus):
    if stat_bonus[0] and stat_bonus[1] and stat_bonus[2] == 10:
        return stat_bonus

    else:
        print(f"Your stat distribution looks like this:\nHp. Bonus: {stat_bonus[0]}\nAtk. Bonus: {stat_bonus[1]}\nDef. Bonus: {stat_bonus[2]}")    
        change = input("Would you like to change the distribution of these stats? (y/n)\nAnswer: ")

        if change.lower() == "n":
            return stat_bonus
        
        elif change.lower() == "y":
            changed_stats = []
            print(f"How would you like to distribute your first stat bonus? {stat_bonus[0]}")
            cs = int(input("1. Hp, 2. Atk, 3. Def\nEnter here: "))
            
            if cs == 1:
                changed_stats.append(stat_bonus[0])
                print(f"How would you like to distribute your second stat bonus? {stat_bonus[1]}")
                csc = int(input("1. Atk, 2. Def\nEnter here: "))
                
                if csc == 1:
                    changed_stats.append(stat_bonus[1])
                    changed_stats.append(stat_bonus[2])
                
                elif csc == 2:
                    changed_stats.append(stat_bonus[2])
                    changed_stats.append(stat_bonus[1])
    
            elif cs == 2:
                print(f"How would you like to distribute your second stat bonus? {stat_bonus[1]}")
                csc = int(input("1. Hp, 2. Def\nEnter here: "))
                
                if csc == 1:
                    changed_stats.append(stat_bonus[1])
                    changed_stats.append(stat_bonus[0])
                    changed_stats.append(stat_bonus[2])
                
                elif csc == 2:
                    changed_stats.append(stat_bonus[2])
                    changed_stats.append(stat_bonus[0])
                    changed_stats.append(stat_bonus[1])

            elif cs == 3:
                print(f"How would you like to distribute your second stat bonus? {stat_bonus[1]}")
                csc = int(input("1. Hp, 2. Atk\nEnter here: "))

                if csc == 1:
                    changed_stats.append(stat_bonus[1])
                    changed_stats.append(stat_bonus[2])
                    changed_stats.append(stat_bonus[0])
                
                elif csc == 2:
                    changed_stats.append(stat_bonus[2])
                    changed_stats.append(stat_bonus[1])
                    changed_stats.append(stat_bonus[0])


            else:
                print("Sorry something went wrong and the stat bonuses will stay the same.")
                return stat_bonus

            return changed_stats
        
        else:
            print("Sorry something went wrong and the stat bonuses will stay the same.")
            return stat_bonus            

# Main code       
def main():
    global cn

    enemies = []
    monster_name = ["Gruffbarb", "Battlebubbles", "Sharpneedles", "Deathgrowl", "Vilescalp", "Smoothheart", "Stinkstink", "Meatblade"]
    players = load_characters()
    mn = 0

    choice = input("Would you like to create a new character? (y/n)\nAnswer: ")
    if choice.lower() == "y":
        stat_bonus = character_choice()
        stat = stat_choice(stat_bonus)
        
        if cn != "Adam":
            hps = (stat[0] + 10)
            atks = ((stat[1]//2) + 3)
            defs = ((stat[2]//4) + 2)
            p1 = Character(cn, hps, atks, defs)
            players.append(p1)
        
        elif cn == "Max":
            hps = (stat[0] + 5)
            atks = ((stat[1]//2) + 2)
            defs = ((stat[2]//4) + 3)
            p1 = Character(cn, hps, atks, defs)
            players.append(p1)

        elif cn == "Aqua":
            hps = (stat[0] + 15)
            atks = ((stat[1]//2) + 3)
            defs = ((stat[2]//4) + 4)
            p1 = Character(cn, hps, atks, defs)
            players.append(p1)

        else:
            hps = 5
            atks = 1
            defs = 0
            p1 = Character(cn, hps, atks, defs)
            players.append(p1)

    if cn != "":
        if cn == "Adam":
            battle = input(f"\nWould you like to proceed to the battlefield, Scrawny {cn}? (y/n)\nAnswer: ")

        elif cn == "Aqua":
            battle = input(f"\nWould you like to proceed to the battlefield, Shmort {cn}? (y/n)\nAnswer: ")
            if battle.lower() == "n":
                print("Sorry the monsters have started their advance to isekai you. GLHF!\n")
        
        elif cn == "Max":
            battle = input(f"\nWould you like to proceed to the battlefield, Skinny Stick Boi? (y/n)\nAnswer: ")
        
        if cn != "Aqua" and cn == "n":
            print("Sorry the monsters have started their advance. GLHF.\n")
        
    random.shuffle(monster_name)
    for _ in range(random.randint(2,4)):
        
        if monster_name[mn] == "Battlebubbles":
            enemies.append(Monster(monster_name[mn], 420, random.randint(5,9), random.randint(4,7)))
            mn += 1

        else:
            enemies.append(Monster(monster_name[mn], random.randint(15,69), random.randint(2,6), random.randint(1,5)))
            mn += 1
    
    
    print("Your characters:")
    for _ in range(len(players)):
        print(f"{players[_]}\n")
    save_character(players)
    
    if len(enemies) == 2:
        print(f"A pair of monsters has apeared.")
        for _ in range(len(enemies)):
            print(f"{enemies[_]}\n")
    
    else:
        print(f"A horde of monsters has apeared.")
        for _ in range(len(enemies)):
            print(f"{enemies[_]}\n")
    
    while len(enemies) != 0 and len(players) != 0:
        new_fight(players, enemies)

    if len(enemies) == 0:
        print("\nThe players won!\nGG!")
        print("\nWould you like to save your character? (y/n)")
        save = input("Enter here: ")
        if save.lower() ==  "y":
            save_character(players)

    elif len(players) == 0:
        print("\nThe Monsters won!")
        print("GAME OVER")

if __name__ == "__main__":
    main()