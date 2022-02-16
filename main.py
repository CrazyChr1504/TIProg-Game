from resourses import Character, Monster
import random
turn = 1
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
        turn += 1
        

def main():
    
    enemies = []
    monster_name = ["Gruffbarb", "Battlebubbles", "Sharpneedles", "Deathgrowl", "Vilescalp", "Smoothheart", "Stinkstink", "Meatblade"]
    players = []
    mn = 0

    p1 = Character("Adam", 14, 8, 0)
    p2 = Character("Viktor", 30, 16, 2)
    players.append(p1)
    players.append(p2)
    
    random.shuffle(monster_name)
    for _ in range(random.randint(2,4)):
        enemies.append(Monster(monster_name[mn], random.randint(14,69), random.randint(1,5), random.randint(4,10)))
        mn += 1
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