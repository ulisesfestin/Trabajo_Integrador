import time
from random import randint, random
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
    points = 15
    print(INPUT_STRENGTH)
    strength = check_input(1, points - 2)
    points -= strength
    print(INPUT_AGILITY)
    agility = check_input(1, points - 1)
    points -= agility
    print(INPUT_CONSTITUTION)
    constitution = check_input(1, points)
    print(INPUT_TYPE)
    print(LIST_OF_TYPES)
    op = check_input(1, 3)
    type = LIST_OF_TYPES[op]

    if type == IF_HUMAN_TYPE:
        human_character = Human(name, age, strength, agility, constitution, type)
        Controller_Characters.add_character_list(human_character)
    if type == IF_ELF_TYPE:
        elf_character = Elf(name, age, strength, agility, constitution, type)
        Controller_Characters.add_character_list(elf_character)
    if type == IF_ORC_TYPE:
        orc_character = Orc(name, age, strength, agility, constitution, type)
        Controller_Characters.add_character_list(orc_character)
    print("Successfully created character.")
    time.sleep(2)


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
        try:
            value = int(input(INPUT_CHOICE))
            if minimum <= value <= maximum:
                return value
            else:
                print(INPUT_ERROR)
        except ValueError:
            print(INPUT_ERROR)


def decision(probability):
    return random() < probability


def health_bar(character):
    string = ""
    for k in range(character.get_health()):
        string += "|"
    string += " %s" % character.get_health()
    return string


def create_enemy():
    print("Generating enemies...")
    for k in range(MAXIMUM_OF_ENEMIES):
        name = ENEMY_NAME
        age = ENEMY_AGE
        strength, agility, constitution = generate_random_attributes(3, ATTRIBUTES_PARAMETER_ENEMY, FIRST_DELIMITER_ENEMY, SECOND_DELIMITER_ENEMY)
        type = ENEMY_TYPE
        enemy_character = Enemy(name, age, strength, agility, constitution, type)
        Controller_Enemies.add_character_list(enemy_character)
    time.sleep(2)


def choose_fighter():
    print(INPUT_LIST_OF_CHARACTERS)
    Controller_Characters.view_character_list()
    character_input = check_input(1, 3)
    Controller_Characters.set_fighter(Controller_Characters.get_character(character_input-1))


def combat():
    if not Controller_Characters.get_fighter():
        print(ERROR_NOT_FIGHTER)
    else:
        fighter = Controller_Characters.get_fighter()
        enemy = Controller_Enemies.get_character(0)
        round = 1
        while True:
            if not fighter.get_is_live():
                print(fighter, "died.")
                Controller_Characters.add_dead_list(Controller_Characters.remove_character_list(Controller_Characters.get_index(fighter)))
                Controller_Characters.remove_fighter()
                break
            elif not enemy.get_is_live():
                print(enemy, "died.")
                Controller_Enemies.add_dead_list(Controller_Enemies.remove_character_list(0))
                fighter.raise_xp(randint(30, 70))
                if decision(PROBABILITY_OF_ITEM):
                    Controller_Characters.generate_item()
                break
            else:
                print("--------------------------------------------------")
                print("Round %s, FIGHT!" % round)
                print("Life bars.")
                print("Fighter", health_bar(fighter))
                print("Enemy", health_bar(enemy))
                print(COMBAT_MENU)
                op = check_input(1, 3)
                if op == 1:
                    fighter.attack(enemy)
                elif op == 2:
                    Controller_Characters.use_item()
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
            create_character()
            create_character()
            create_character()
            create_enemy()
            while True:
                if not Controller_Characters.get_character_list():
                    print("You lost all your characters.")
                    print("GAME OVER")
                    return
                if not Controller_Enemies.get_character_list():
                    print("You defeated all the enemies! \nCongratulations, you won!")
                    return
                print(SECONDARY_MENU)
                op = check_input(1, 5)
                if op == 1:
                    choose_fighter()
                elif op == 2:
                    combat()
                elif op == 3:
                    view_stats()
                    input(ENTER)
                elif op == 4:
                    Controller_Characters.view_inventory()
                    input(ENTER)
                elif op == 5:
                    close()
                    return
                else:
                    print(INPUT_ERROR)
        elif op == 2:
            print(CREDITS)
            time.sleep(2)
        elif op == 3:
            close()
            break
        else:
            print(INPUT_ERROR)


menu()

