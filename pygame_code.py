# Imports
from resourses import Character, Monster, save_character, load_characters
from time import sleep
import random, pygame

# Global variables
turn = 1
game = 1
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

def pygame_prints(screen, AZURE, players):
    
    render_fonts = []
    font = pygame.font.Font("freesansbold.ttf", 26)
    space = 4
    fs = 26
    y = 10
    x = 10
    text = ""

    for i in range(len(players)):
        text += players[i].__str__()
    for i, line in enumerate(text.split('\n')):
        txt_surf = font.render(line, True, pygame.Color('black'))
        txt_rect = txt_surf.get_rect()
        txt_rect.topleft = (x, y + i * (fs + space))
        render_fonts.append((txt_surf, txt_rect))
    
    screen.fill(AZURE)
    for txt_surf, txt_rect in render_fonts:
        screen.blit(txt_surf, txt_rect)
    pygame.display.flip()

def enemies_prints(enemies, screen):
    render_fonts = []
    font = pygame.font.Font("freesansbold.ttf", 26)
    space = 4
    fs = 26
    y = 10
    x = 880
    text = ""

    for i in range(len(enemies)):
        text += enemies[i].__str__()
    for i, line in enumerate(text.split('\n')):
        txt_txt = font.render(line, True, pygame.Color('black'))
        text_rect = txt_txt.get_rect()
        text_rect.topleft = (x, y + i * (fs + space))
        render_fonts.append((txt_txt, text_rect))

    for txt_txt, text_rect in render_fonts:
        screen.blit(txt_txt, text_rect)
    pygame.display.update()

def end_prints(screen, enemies, players):
    pygame.init()
    AZURE = (178, 216, 255)
    size = [1540, 800]
    screen1 = pygame.display.set_mode((size))
    screen1.fill(AZURE)
    if len(enemies) == 0:
        screen1.fill(AZURE)
        text_font1 = pygame.font.Font("freesansbold.ttf", 70)
        text1 = "YOU WIN!!"
        text_text1 = text_font1.render(text1,True, (0,0,0))
        text_rect1 = text_text1.get_rect()
        text_rect1.center = (770,400)
        screen1.blit(text_text1, text_rect1)

    elif len(players) == 0:
        screen1.fill(AZURE)
        render_fonts = []
        font = pygame.font.Font("freesansbold.ttf", 70)
        space = 4
        fs = 26
        y = 400
        x = 770
        txt = "GAME OVER!\nMONSTERS WON!"

        for i, line in enumerate(txt.split('\n')):
            txt_txt = font.render(line, True, pygame.Color('black'))
            text_rect = txt_txt.get_rect()
            text_rect.topleft = (x, y + i * (fs + space))
            render_fonts.append((txt_txt, text_rect))

        for txt_txt, text_rect in render_fonts:
            screen1.blit(txt_txt, text_rect)

    elif turn >= 200:
        screen1.fill(AZURE)
        text_font2 = pygame.font.Font("freesansbold.ttf", 70)
        text2 = "YOU HAVE DIED!"
        text_text2 = text_font2.render(text2,True, (0,0,0))
        text_rect2 = text_text2.get_rect()
        text_rect2.center = (770,400)
        screen1.blit(text_text2, text_rect2)

    else:
        turn_prints(screen, AZURE, players, enemies)

    sleep(3)
    pygame.quit()

def turn_prints(screen, AZURE, players, enemies):
    global turn
    global game
    participants = players + enemies
    random.shuffle(participants)

    font = pygame.font.Font("freesansbold.ttf", 26)
    space = 4
    fs = 26
    y = 400
    x = 50

    for char in participants:
        #if turn >= 200:
            #end_prints(screen, enemies, players, AZURE)
        render_fonts = []
        if len(players) == 0 or len(enemies) == 0:
            break
        text = ""
        text += f"Turn: {turn}\n" 
        target = ""
        # Check if player or monster
        if char in players:
            target = random.choice(enemies) 
        else:
            target = random.choice(players)

        target.take_damage(char.attack())
        if target.get_health() == 0:
            text += f"{char.get_name()} has attacked {target.get_name()}.\n"
            text += f"{char.get_name()} has killed {target.get_name()}.\n"
            if(type(target) == Monster):
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
            sleep(0.5)
        
        else:
            text += f"{char.get_name()} was attacked by {target.get_name()}.\n"
            text += f"{char.get_name()} has {target.get_health()} hp left.\n"
        
        for i, line in enumerate(text.split('\n')):
            text_surf = font.render(line, True, pygame.Color('black'))
            text_rect = text_surf.get_rect()
            text_rect.topleft = (x, y + i * (fs + space))
            render_fonts.append((text_surf, text_rect))
        
        

        pygame_prints(screen, AZURE, players)
        enemies_prints(enemies, screen)
        for text_surf, text_rect in render_fonts:
            screen.blit(text_surf, text_rect)
        pygame.display.update()
        if len(players) == 0 or len(enemies) == 0:
            if len(enemies) == 0:
                screen.fill(AZURE)
                text_font1 = pygame.font.Font("freesansbold.ttf", 70)
                text1 = "YOU WIN!!"
                text_text1 = text_font1.render(text1,True, (0,0,0))
                text_rect1 = text_text1.get_rect()
                text_rect1.center = (770,400)
                screen.blit(text_text1, text_rect1)

            elif len(players) == 0:
                screen.fill(AZURE)
                render_fonts = []
                font = pygame.font.Font("freesansbold.ttf", 70)
                space = 4
                fs = 26
                y = 400
                x = 770
                txt = "GAME OVER!\nMONSTERS WON!"

                for i, line in enumerate(txt.split('\n')):
                    txt_txt = font.render(line, True, pygame.Color('black'))
                    text_rect = txt_txt.get_rect()
                    text_rect.topleft = (x, y + i * (fs + space))
                    render_fonts.append((txt_txt, text_rect))

                for txt_txt, text_rect in render_fonts:
                    screen.blit(txt_txt, text_rect)
            pygame.display.flip()
            sleep(2)
            pygame.quit()
        sleep(0.5)
        turn += 1

# Main code       
def main():
    pygame.init()
    global cn
    global game
    running = 0
    enemies = []
    enemies_cl = []
    running = True
    name_list = []
    player_list = []
    option = 0
    clock = pygame.time.Clock()
    AZURE = (178, 216, 255)
    size = [1540, 810]
    screen = pygame.display.set_mode((size))
    screen.fill(AZURE)

    players = load_characters()
    print("Your characters:")
    for i in range(len(players)):
        print(f"{players[i]}\n")
    save_character(players)

    mn = 0
    monster_name = ["Gruffbarb", "Sharpneedles", "Deathgrowl", "Vilescalp", "Smoothheart", "Stinkstink", "Meatblade"]
    random.shuffle(monster_name)
    for _ in range(random.randint(2,4)):
        
        if monster_name[mn] == "Battlebubbles":
            enemies.append(f"{(monster_name[mn])}/{420}/{random.randint(5,9)}/{random.randint(4,6)}\n")
            enemies_cl.append(Monster(monster_name[mn], 420, random.randint(5,9), random.randint(4,6)))
            mn += 1

        else:
            enemies.append(f"{(monster_name[mn])}/{random.randint(15,69)}/{random.randint(3,7)}/{random.randint(1,4)}\n")
            enemies_cl.append(Monster(monster_name[mn], random.randint(15,69), random.randint(3,7), random.randint(1,4)))
            mn += 1

    with open("character_file.txt", "r", encoding="utf8") as f:
        for i in f.readlines():
            player_list.append(i)
        f.close()
    for i in range(len(players)):
        name_list.append(players[i].__str__())


    pygame.display.set_caption("Hell-mode Battle Simulation")
    text_font = pygame.font.Font("freesansbold.ttf", 26)
    text = "Would you like to see your characters and start the battle simulation? (Y/N)"
    text_text = text_font.render(text,True, (0,0,0))
    text_rect = text_text.get_rect()
    text_rect.center = (770,100)
    screen.blit(text_text, text_rect)
    pygame.display.flip()

    mn = 0
    players = load_characters()
    while running:
        clock.tick(10)
        pygame.display.flip()

        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN:
                if option == 0:
                    press = pygame.key.name(event.key)
                    pygame.event.clear(eventtype=None)
                    if press == "y":
                        option = 1
                    elif press == "n":
                        option = 2

                if option == 3:
                    next_press = pygame.key.name(event.key)
                    pygame.event.clear(eventtype=None)
                    if next_press == "y":
                        enemies_prints(enemies, screen)
                        option = 4
                    elif next_press == "n":
                        option = 2
                if option == 4:
                    while game == running:
                        turn_prints(screen, AZURE, players, enemies_cl)
                else:
                    continue
                pygame.event.clear(eventtype=None)
            if event.type == pygame.QUIT:
                pygame.quit()

        if option == 1:
            if len(players)>1:
                pygame_prints(screen, AZURE, players)
            else:        
                text_font = pygame.font.Font("freesansbold.ttf", 26)
                text_text = text_font.render("",True, (0,0,0))
                text_text = text_font.render(name_list[0],True, (0,0,0))
                text_rect = text_text.get_rect()
                text_rect.center = (250,175)
                screen.blit(text_text, text_rect)
            option = 3
            pygame.display.flip()

        if option == 2:
            screen.fill(AZURE)
            text_font = pygame.font.Font("freesansbold.ttf", 26)
            text = "Thanks for playing. Have a nice day!"
            text_text = text_font.render(text,True, (0,0,0))
            text_rect = text_text.get_rect()
            text_rect.center = (770,100)
            screen.blit(text_text, text_rect)
            pygame.display.flip()
            sleep(2)
            pygame.quit()
                

    choice = " "
    # choice = input("Would you like to create a new character? (y/n)\nAnswer: ")
    if choice.lower() == "y":
        stat_bonus = character_choice()
        stat = stat_choice(stat_bonus)
        
        if cn == "Max":
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

        elif cn == "Adam":
            hps = 5
            atks = 1
            defs = 0
            p1 = Character(cn, hps, atks, defs)
            players.append(p1)
            
        else:
            hps = (stat[0] + 10)
            atks = ((stat[1]//2) + 3)
            defs = ((stat[2]//4) + 2)
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