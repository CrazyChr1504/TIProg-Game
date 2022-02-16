from resourses import Character, Monster
import random

def new_fight(players: list, enemies: list):

    participants = players + enemies # Puts together the participants in one list
    random.shuffle(participants)

    for char in participants:
        target = ""
        # Check if player or monster
        if char in players:
            target = random.choice(enemies) 
        else:
            target = random.choice(players)

        target.take_damage(char.attack())
        if target.get_health() == 0:
            print(f"{char.get_name()} was attack by {target.get_name()}.")
            print(f"{char.get_name()} has killed {target.get_name()}.")
            if(type(target) == Monster):
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        
        else:
            print(f"{target.get_name()} was attack by {char.get_name()}.")
            print(f"{target.get_name()} has {target.get_health()} hp left.")
        
        if len(players) == 0 or len(enemies) == 0:
            break

def main():
    
    enemies = []
    monster_name = ["Gruffbarb",]
    players = []

    nick = Character("Nick", 15, 3, 1)
    emy = Character("Emy", 20, 6, 5)
    players.append(nick)
    players.append(emy)
    
    for i in range(random.randint(2,4)):
        enemies.append(Monster)
    

    #fight(emy, enemies)

    while len(enemies) != 0 and len(players) != 0:
        new_fight(players, enemies)

    if len(enemies) == 0:
        print("The players won!")
    elif len(players) == 0:
        print("The Monsters won!")
        print("GAME OVER")
    
if __name__ == "__main__":
    main()