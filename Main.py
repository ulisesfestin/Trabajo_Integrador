from random import *
from Character import Character
from Human import Human
from Elf import Elf
from Orc import Orc
from Enemy import Enemy
from GSC_Constants import *
from Controller import *
Characters = Controller()
Enemies = Controller()


def create_character():
    name = str(input(INPUT_NAME))
    age = int(input(INPUT_AGE))
    def Distribute_score():
        global strength, agility, constitution
        strength = 0
        agility = 0
        constitution = 0
        score = 15
        while score > 0:
            print(INPUT_SCORE1, score, INPUT_SCORE2)
            strength = int(input(INPUT_STRENGTH))
            score = score-strength  
            if score < 0:
                Distribute_score()
            else:
                pass
            print(INPUT_SCORE1, score , INPUT_SCORE2)
            agility = int(input(INPUT_AGILITY))
            score = score-agility
            if score < 0:
                Distribute_score()
            else:
                pass
            print(INPUT_SCORE1, score , INPUT_SCORE2)
            constitution = int(input(INPUT_CONSTITUTION))
            score = score-constitution
            if score < 0:
                Distribute_score()
            else:
                pass
    Distribute_score()
    type = str(input(INPUT_TYPE))

    if type == IF_HUMAN_TYPE:
        human_character = Human(name, age, strength, agility, constitution, type)
        Characters.add_character_list(human_character)
    if type == IF_ELF_TYPE:
        elf_character = Elf(name, age, strength, agility, constitution, type)
        Characters.add_character_list(elf_character)
    if type == IF_ORC_TYPE:
        orc_character = Orc(name, age, strength, agility, constitution, type)
        Characters.add_character_list(orc_character)
        print(orc_character.get_attributes())


def delete_character():
    Characters.view_character_list()
    index = int(input(INPUT_DELETE_CHARACTER))
    Characters.delete_character_list(index - 1)


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
    name = str(input(INPUT_NAME))
    age = int(input(INPUT_AGE))
    strength, agility, constitution = generate_random_attributes(3, ATTRIBUTES_PARAMETER_ENEMY, FIRST_DELIMITER_ENEMY, SECOND_DELIMITER_ENEMY)
    type = ENEMY_TYPE

    enemy_character = Enemy(name, age, strength, agility, constitution, type)
    Enemies.add_character_list(enemy_character)


def choose_character():
    pass


def combat():
    dice = randint(1, 6) + randint(1, 6)
    if dice in FIRST_GROUP:
        return FIRST_GROUP_DAMAGE
    elif dice in SECOND_GROUP:
        return SECOND_GROUP_DAMAGE
    elif dice in THIRD_GROUP:
        return THIRD_GROUP_DAMAGE
    else:
        return CRITICAL_DAMAGE



create_character()
create_character()
create_character()
delete_character()
Characters.view_character_list()
create_enemy()
Enemies.view_character_list()
#print(combat())
