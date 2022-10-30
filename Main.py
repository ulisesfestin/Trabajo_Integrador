import time
from random import *
from Controller import *
from Elf import Elf
from Enemy import Enemy
from Human import Human
from Orc import Orc

Controller_Characters = Controller(MAXIMUM_OF_CHARACTERS)
Controller_Enemies = Controller(MAXIMUM_OF_ENEMIES)


def create_character():
    name = str(input(INPUT_NAME))
    age = int(input(INPUT_AGE))
    strength = int(input(INPUT_STRENGTH))
    agility = int(input(INPUT_AGILITY))
    constitution = int(input(INPUT_CONSTITUTION))
    type = str(input(INPUT_TYPE))

    if type == IF_HUMAN_TYPE:
        human_character = Human(name, age, strength, agility, constitution, type)
        Controller_Characters.add_character_list(human_character)
    if type == IF_ELF_TYPE:
        elf_character = Elf(name, age, strength, agility, constitution, type)
        Controller_Characters.add_character_list(elf_character)
    if type == IF_ORC_TYPE:
        orc_character = Orc(name, age, strength, agility, constitution, type)
        Controller_Characters.add_character_list(orc_character)


def delete_character():
    Controller_Characters.view_character_list()
    print(INPUT_DELETE_CHARACTER)
    index = check_input(1, 3)
    Controller_Characters.delete_character_list(index - 1)


def generate_random_attributes(number_of_attributes, total, range1, range2):
    sum_of_numbers = EMPTY_INT
    list_of_numbers = []
    while sum_of_numbers != total:
        sum_of_numbers = EMPTY_INT
        list_of_numbers = []
        for index in range(number_of_attributes):
            number = randint(range1, range2)
            list_of_numbers.append(number)
            sum_of_numbers += number
    return list_of_numbers


def check_input(minimum, maximum):
    while True:
        value = int(input("Choose an option from %s to %s: " % (minimum, maximum)))
        if minimum <= value <= maximum:
            return value
        else:
            print("Input error.")


def create_enemy():
    for k in range(MAXIMUM_OF_ENEMIES):
        name = "Death Soldier"
        age = 1500
        strength, agility, constitution = generate_random_attributes(3, ATTRIBUTES_PARAMETER_ENEMY, FIRST_DELIMITER_ENEMY, SECOND_DELIMITER_ENEMY)
        type = ENEMY_TYPE
        enemy_character = Enemy(name, age, strength, agility, constitution, type)
        Controller_Enemies.add_character_list(enemy_character)


def choose_fighter():
    print("List of characters, choose one.")
    Controller_Characters.view_character_list()
    character_input = check_input(1, 3)
    Controller_Characters.set_fighter(Controller_Characters.get_character(character_input-1))


def combat():           # En desarrollo
    if not Controller_Characters.get_fighter():
        print("You have not selected your fighter.")
    else:
        fighter = Controller_Characters.get_fighter()
        enemy = Controller_Enemies.get_character(0)
        round = 1
        while True:
            if not fighter.get_is_live():
                print(fighter, "died.")
                Controller_Characters.add_dead_list(Controller_Characters.remove_character_list(Controller_Characters.get_index(fighter)))
                break
            elif not enemy.get_is_live():
                print(enemy, "died.")
                Controller_Enemies.add_dead_list(Controller_Enemies.remove_character_list(0))
                fighter.raise_xp()
                break
            else:
                print("--------------------------------------------------")
                print("Round %s, FIGHT!" % round)
                print(COMBAT_MENU)
                op = check_input(1, 3)
                if op == 1:
                    fighter.attack(enemy)
                elif op == 2:
                    "view inventory"
                elif op == 3:
                    print("You ran away from the fight.")
                    break
                enemy.attack(fighter)
                round += 1
                input("Press enter to continue.")


def view_stats():
    Controller_Characters.view_stats()


def close():
    print('Closing...')
    time.sleep(2)
    print("Thanks for playing!")


def menu():
    while True:
        print(MAIN_MENU)
        op = check_input(1, 3)
        if op == 1:
            print(START_GAME)
            input()
            human_character = Human("Ulises Festin", 20, 8, 4, 3, "Human")  # Solo de prueba
            Controller_Characters.add_character_list(human_character)
            elf_character = Elf("Aldana Moreno", 20, 5, 4, 6, "Elf")
            Controller_Characters.add_character_list(elf_character)
            orc_character = Orc("Pablo Balastegui", 20, 1, 5, 9, "Orc")
            Controller_Characters.add_character_list(orc_character)
            create_enemy()
            while True:
                print(SECONDARY_MENU)
                op = check_input(1, 5)
                if op == 1:
                    choose_fighter()
                elif op == 2:
                    combat()
                elif op == 3:
                    view_stats()
                elif op == 4:
                    "view_inventory()"
                elif op == 5:
                    close()
                    return
                else:
                    print(INPUT_ERROR)
        elif op == 2:
            print(CREDITS)
        elif op == 3:
            close()
            break
        else:
            print(INPUT_ERROR)


menu()


"""
human_character = Human("Ulises Festin", 20, 8, 4, 3, "Human")
Controller_Characters.add_character_list(human_character)
elf_character = Elf("Aldana Moreno", 20, 5, 4, 6, "Elf")
Controller_Characters.add_character_list(elf_character)
orc_character = Orc("Pablo Balastegui", 20, 1, 5, 9, "Orc")
Controller_Characters.add_character_list(orc_character)
#Controller_Characters.view_character_list()
create_enemy()
#Controller_Enemies.view_character_list()
choose_character()
combat()
#Controller_Enemies.view_stats()"""