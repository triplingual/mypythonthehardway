# I use modules from colorama: http://pypi.python.org/pypi/colorama

from sys import exit
from time import sleep
from random import choice
from colorama import init, Fore, Style
init(autoreset = True)

# Start variables.
dive = False
climb = False
stones = []
fullstones = ["o", "f", "m"]
slime = 0
elf = 0
crab = 0
jelly = 0
troll = 0
dragon = 0
level = 1

# Player stats.
health = 100
max_health = 100
mana = 10
max_mana = 10
damage = range(5, 16)
mana_cost = 2
heal = 40

# Enemy stats
weak_health = 50
weak_damage = range(10, 21)
strong_health = 75
strong_damage = range(15, 26)
boss_health = 500
boss_damage = range(50, 76)

# Level up function.
def lvlup():
    global max_health, health, damage, heal, level
    max_health = 500
    health = max_health
    damage = range(35, 61)
    heal = 150
    level = 2


# Function for the temple entrance.
# set() compares the elements of the two lists regardless of order. It's faster than sorting them first and then comparing.
# Could have used .issubset() as well, it checks if all the elements in one list exists in another list.
def start():
    print "\nYou're now standing in front of the holy temple. There are three other areas in this world: The forest, the mountain and the ocean. Where do you want to go?"
    
    while True:
        next = raw_input("> ").lower()
        
        if "temple" in next and not set(fullstones) == set(stones):
            print "You need to have the three stones before you can enter. You have these stones so far: %r" % stones
        elif "temple" in next and set(fullstones) == set(stones):
            temple()
        elif "forest" in next:
            forest()
        elif "mountain" in next:
            mountain()
        elif "ocean" in next:
            ocean()
        else:
            print "You don't know where this area is."


# Function for the forest.
def forest():
    global slime
    if slime == 0:
        print "\nYou have arrived in the forest. There is a slime blocking your path. You will have to kill it if you want to continue. Type attack to fight or flee to return to the temple entrance."
        fight("easy", "slime")
        print "Congratulations, you beat the slime!"
        slime = 1
        sleep(1)
        forest()
    else:
        print "\nYou are in the forest. To your left is a clearing where you can heal, to your right is the way to the deep part of the forest. Where do you want to go?"
        while True:
            next = raw_input("> ").lower()

            if "clearing" in next or "left" in next:
                clearing()
            elif "deep" in next or "right" in next:
                deep()
            elif "return" in next or "temple" in next:
                start()
            else:
                print "You can only go to the clearing or the deep part of the forest. You can also return to the temple."

# Function for the clearing.
def clearing():
    global health
    print "\nYou enter the clearing, which fills you with positive energy. Your health has regained. You now have 100 health."
    health = max_health
    sleep(1)
    print "You don't have anything else to do in the clearing, so you return to where you came from."
    sleep(1)
    forest()

# Function for the deep part of the forest.
def deep():
    if elf == 0:
        print "\nAs you go through the deep part of the forest you come across a sacred grove. This must be where the forest stone is. Unfortunately an elf is guarding the stone. You will have to kill him in order to get the stone. Do you want to go to the grove, or do you want to return to the temple entrance?."
        while True:
            next = raw_input("> ")

            if "grove" in next:
                grove()
            elif "return" in next or "temple" in next:
                start()
            else:
                print "You have to either return to the temple or go to the grove."
    else:
        print "\nYou are in the deep part of the forest. You can either go to the sacred grove or return to the forest entrance."
        while True:
            next = raw_input("> ")

            if "grove" in next:
                grove()
            elif "return" in next or "forest" in next or "entrance" in next:
                forest()
            else:
                print "You must either go to the grove or return to the forest entrance."

# Function for the grove.
def grove():
    global elf, stones
    if elf == 0:
        print "\nAs you enter the grove you're spotted by the elf. He attacks you and you are forced to fight him!"
        combat("hard", "elf")
        print "Congratulations, you got the forest stone. You will now return to the temple entrance."
        elf = 1
        stones.append('f')
        sleep(1)
        start()
    else:
        print "\nYou enter the sacred grove, but you already have the stone here. There is nothing more to do. You return to the temple gate."
        sleep(1)
        start()


# Function for the mountain.
def mountain():
    global troll
    if troll == 0:
        print "\nYou have arrived at the mountain. A giant troll is blocking your path. Do you flee, or do you fight?"
        fight("easy", "troll")
        troll = 1
        print "Congratulations, you beat the troll. You have %r health left." % health
        sleep(1)
        mountain()        
    elif dragon == 0:
        print "\nYou are in the mountains. You see a traveller who has set up camp in the distance. At the top of the mountains is a dragon. You suspect that this is where the mountain stone is. There is also a cave nearby. Where do you want to go?"
        mountain_travel()
    else:
        print "\nYou are in the mountains. You can either go to the traveller, visit the cave or go to the top."
        mountain_travel()

# Function for the cave.
def cave():
    global climb
    if climb == False:
        print "\nYou enter the cave and find some climbing equipment on the ground. What a lucky day! Now you can get to the top of the mountain."
        climb = True
        sleep(1)
        print "Now that you have the equipment you return to the mountain."
        sleep(1)
        mountain()
    else:
        print "\nYou have already done everything there is to do in the cave. You return to the mountain."
        sleep(1)
        mountain()

# Function for the traveller.
def traveller():
    global health
    print "\nThe traveller greets you as you approach. He invites you inside for a nice meal. You are healed to full health. You have 100 health."
    health = max_health
    sleep(1)
    print "You say farewell to the traveller and return to the mountain."
    sleep(1)
    mountain()
    
# Function for the top.
def top():
    global dragon, stones
    while True:
        if dragon == 0:
            print "\nAs you reach the top of the mountain you encounter a dragon guarding the stone. You will have to kill it in order to get it. Do you fight or flee?"
            fight("hard", "dragon")
            dragon = 1
            stones.append('m')
            print "You beat the dragon! Congratulations. You now have the mountain stone. You return to the temple entrance."
            sleep(1)
            start()
        else:
            print "\nYou reach the top of the mountain, but you already have the stone. You return to the temple."
            sleep(1)
            start()


# Function for the ocean.
def ocean():
    global crab
    if crab == 0:
        print "\nYou encounter a giant crab on the beach and you have to kill it to continue. Do you fight or flee?"
        fight("easy", "crab")
        print "Congratulations, you beat the crab."
        crab = 1
        sleep(1)
        ocean()
    elif jelly == 0:
        print "\nYou are at the beach. You think the ocean stone is in a cave under water, so you will have to dive down there in order to get it. At the beach there is a shrine and an abandoned camp. Where do you want to go?"
        ocean_travel()
    else:
        print "\nYou are at the beach. You see a shrine and an abandoned camp. You can also dive to the underwater cave. Where do you want to go?"
        ocean_travel()

# Function for the camp.
def camp():
    global dive
    if dive == False:
        print "\nYou go to the abandoned camp. You find some working diving equipment here. You can now dive to the ocean stone."
        dive = True
        sleep(1)
        print "You return to the beach."
        sleep(1)
        ocean()
    else:
        print "\nYou already have the diving equipment from the camp. You can't do anything else here. You go back to the beach."
        sleep(1)
        ocean()

# Function for the shrine.
def shrine():
    global health
    print "\nYou approach the shrine. You feel your wounds healing. You are now at full health. You have 100 health."
    sleep(1)
    health = max_health
    print "You return to the beach."
    sleep(1)
    ocean()

# Function for the underwater cave.
def depth():
    global jelly, stones
    if jelly == 0:
        print "\nAs you dive underwater you approach a giant jellyfish guarding the stone. You have to kill this if you want to continue. Do you want to flee or fight?"
        fight("hard", "jellyfish")
        print "Congratulations, you beat the jellyfish. Now you have the ocean stone."
        jelly = 1
        stones.append('o')
        sleep(1)
        print "You return to the temple entrance."
        sleep(1)
        start()
    else:
        print "\nYou dive around for a while looking for other things of interest, but since you already have the ocean stone you find nothing. You return to the temple entrance."
        sleep(1)
        start()


# Function for the temple.
def temple():
    if level == 1:
        lvlup()
        print "\nAs you approach the door with the three stones you feel your power increasing. You now have more health and damage. The door opens and you enter the temple."
        sleep(1)
    else:
        print "\nThe gate is already open so you can go freely through it."
        sleep(1)
    print "\nYou are inside the temple. There is a huge elemental guardian protecting the treasure. You will have to kill him if you want the treasure. Do you want to flee or fight?"
    fight("boss", "Guardian")
    print "Congratulations, you got the treasure! You won the game!"
    exit()    


# Defines the function for travelling in the ocean.
def ocean_travel():
    while True:
        next = raw_input("> ")

        if "shrine" in next:
            shrine()
        elif "camp" in next:
            camp()
        elif "dive" in next and dive == False:
            print "You need diving equipment before you can go to the depths."
        elif "dive" in next and dive == True:
            depth()
        elif "return" in next or "temple" in next:
            start()
        else:
            print "You need to either go to the shrine, the camp or dive. You can also return to the temple."

# Defines the function for travelling in the mountains.
def mountain_travel():
    while True:
            next = raw_input("> ")

            if "traveller" in next or "camp" in next:
                traveller()
            elif "top" in next and climb == False:
                print "You need climbing equipment in order to climb the mountain."
            elif "top" in next and climb == True:
                top()
            elif "cave" in next:
                cave()
            elif "return" in next or "temple" in next:
                start()
            else:
                print "You need to go to either the traveller, the cave or the top. You can also return to the temple."


# Defines the function that asks if user wants to fight.
def fight(diff, mob):
    while True:
        fight = raw_input("> ").lower()

        if "fight" in fight or "attack" in fight:
            combat(diff, mob)
            break
        elif "flee" in fight or "run" in fight:
            start()
        else:
            print "You have to either fight or flee."

# Defining the function that prints the introduction text.
def first():
    print "\nYou have heard of a treasure that lies within the holy temple, but to enter you're required to find three magic stones."
    print "You can find one of these stones in the mountains, one in the ocean, and one in the forest."
    start()


# Combat function.
def combat(diff, mob):
    global health, mana
    
    # Checks for difficulty and sets stats accordingly.
    if diff == "easy":
        mob_health = weak_health
        mob_damage = weak_damage
    elif diff == "hard":
        mob_health = strong_health
        mob_damage = strong_damage
    elif diff == "boss":
        mob_health = boss_health
        mob_damage = boss_damage
    else:
        print "Unknown difficulty, aborting!"
        exit()

    # Set start colors.    
    you = color("cyan", 'You')
    mob = color("yellow", '%s' % mob)
    health_c = color("magenta", '%d health' % health)
    mob_health_c = color("magenta", '%d health' % mob_health)
    mana_c = color("cyan", '%d mana' % mana)
    mana_co = color("cyan", '%d mana' % mana_cost)

    # Prints start text.
    print "\nStarting fight between %s and %s. %s have %s and %s while the %s has %s." % (you, mob, you, health_c, mana_c, mob, mob_health_c)
    print "Type 'attack' to attack the %s  and type 'heal' to heal yourself. It costs %s to heal." % (mob, mana_co)

    # The combat coninues while everyone has above 0 health.
    while mob_health > 0 and health > 0:
        print ""

        while True:
            action = raw_input("> ")

            # Checks for user action.
            # If attack.
            if action == "attack":
                dam = choice(damage)        
                mob_health -= dam
                dam_c = color("red", '%d damage' % dam)
                mob_health_c = color("magenta", '%d health' % mob_health)
                break
            # If heal.
            elif action == "heal" and mana > 0:
                # If at max health
                if health >= max_health:
                    print "You already have max health, you can't heal."
                # If you have lost less health than you will heal.
                elif max_health - health <= heal:
                    heals = max_health - health
                    health = max_health
                    mana -= mana_cost
                    heal_c = color("green", '%d health' % heals)
                    health_c = color("magenta", '%d health' % health)
                    mana_c = color("cyan", '%d mana' % mana)
                    print "%s healed %s. %s now have %s left. You have %s left." % (you, heal_c, you, health_c, mana_c)
                    break 
                # If you have lost more health than you will heal.
                else:
                    health += heal
                    mana -= mana_cost
                    heal_c = color("green", '%d health' % heal)
                    health_c = color("magenta", '%d health' % health)
                    mana_c = color("cyan", '%d mana' % mana)
                    print "%s healed %s. %s now have %s left. You have %s left." % (you, heal_c, you, health_c, mana_c)
                    break
            # If you don't type heal or attack.
            elif action == "heal" and mana <= 0:
                print "You don't have enough mana to heal. It costs 2 mana."
            else:
                print "You need to either attack or heal."
                
        # Runs after the user input loop is done. Checks for mob health.
        if mob_health <= 0:
            print "%s deal %s to the %s! It has no more health left." % (you, dam_c, mob)
            break
        elif mob_health > 0 and action == "attack":
            print "%s deal %s to the %s! It has %s left." % (you, dam_c, mob, mob_health_c)            
        sleep(1)

        # Runs after it has checked for mob health and the mob is still alive.
        dam = choice(mob_damage)
        health -= dam
        dam_c = color("red", '%d damage' % dam)
        health_c = color("magenta", '%d health' % health) 

        # Checks for player health. Breaks if health is at or below zero.       
        if health <= 0:
            print "The %s deals %s to %s. You have no more health left." % (mob, dam_c, you)
            break
        else:
            print "The %s deals %s to %s. You have %s left." % (mob, dam_c, you, health_c)            
        sleep(1)
        # Continues loop if it has not been broken yet.

    # Information on who wins the fight. Runs after previous loop is broken.
    if mob_health <= 0:
        print "\nYou win the fight."
        mana = max_mana
    elif health <= 0:
        print "\nYou lose the fight."
        mana = max_mana
        ress()
    else:
        print "Error, no one lost the fight. Aborting!"
        exit()


# The resurrection function.
def ress():
    global health
    print "You died. But fortunately you're immortal so you are returned to the starting area with full health.\n"
    health = max_health
    start()


# Color function.
def color(col, text):
    if col == 'red':
        red =Fore.RED + Style.BRIGHT + '%s' % text + Fore.RESET + Style.RESET_ALL
        return red
    elif col == 'cyan':
        cyan = Fore.CYAN + Style.BRIGHT + '%s' % text + Fore.RESET + Style.RESET_ALL
        return cyan
    elif col == 'yellow':
        yellow = Fore.YELLOW + Style.BRIGHT + '%s' % text + Fore.RESET + Style.RESET_ALL
        return yellow
    elif col == 'green':
        green = Fore.GREEN + Style.BRIGHT + '%s' % text + Fore.RESET + Style.RESET_ALL
        return green
    elif col == 'magenta':
        magenta = Fore.MAGENTA + Style.BRIGHT + '%s' % text + Fore.RESET + Style.RESET_ALL
        return magenta
    else:
        print "Error, not a color. Aborting!"
        exit()


# Runs the start function.
first()