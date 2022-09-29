from random import *
from Character import Character
from Human import Human
from Elf import Elf
from Orc import Orc
from Enemy import Enemy
from GSC_Constants import *
from Controller import *
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
    index = int(input(INPUT_DELETE_CHARACTER))
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


def create_enemy():
    for k in range(MAXIMUM_OF_ENEMIES):
        name = "Death Soldier"
        age = 1500
        strength, agility, constitution = generate_random_attributes(3, ATTRIBUTES_PARAMETER_ENEMY, FIRST_DELIMITER_ENEMY, SECOND_DELIMITER_ENEMY)
        type = ENEMY_TYPE
        enemy_character = Enemy(name, age, strength, agility, constitution, type)
        Controller_Enemies.add_character_list(enemy_character)


def choose_character():
    print("List of characters, choose one.")
    Controller_Characters.view_character_list()
    character_input = int(input(""))
    Controller_Characters.set_fighter(Controller_Characters.get_character(character_input-1))


def combat():           # En desarrollo
    """fighter = Controller_Characters.get_fighter()
    enemy = Controller_Enemies.get_character(0)
    round = 1
    while True:
        print("Round %s, FIGHT!" % round)
        fighter.attack(enemy) if enemy.check_health() else break
        enemy.attack(fighter) if fighter.check_health() else break
        round += 1"""
    pass




human_character = Human("Ulises Festin", 20, 8, 4, 3, "Human")
Controller_Characters.add_character_list(human_character)
elf_character = Elf("Aldana Moreno", 20, 8, 4, 3, "Elf")
Controller_Characters.add_character_list(elf_character)
orc_character = Orc("Pablo Balastegui", 20, 8, 4, 3, "Orc")
Controller_Characters.add_character_list(orc_character)
#Controller_Characters.view_character_list()
create_enemy()
Controller_Enemies.view_character_list()
#choose_character()
#combat()
