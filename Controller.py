from GSC_Constants import *
from random import randint
from Items import Items



class Controller:
    def __init__(self, max_of_characters):
        self.__list_of_characters = []
        self.__dead_list = []
        self.__fighter = None
        self.__choose = False
        self.__max = max_of_characters
        self.__inventory = []

    def add_character_list(self, character):
        if self.check_maximum_characters():
            self.__list_of_characters.append(character)
        else:
            return print(ERROR_MAXIMUM_CHARACTERS)

    def remove_character_list(self, index):
        return self.__list_of_characters.pop(index)

    def add_dead_list(self, character):
        self.__dead_list.append(character)

    def view_character_list(self):
        for index in range(len(self.__list_of_characters)):
            print(str(index + 1) + ")", self.__list_of_characters[index].get_name(), "-->", self.__list_of_characters[index].get_type())

    def delete_character_list(self, character):
        self.__list_of_characters.pop(character)
        return print(CHARACTER_DELETED)

    def check_maximum_characters(self):
        if len(self.__list_of_characters) < self.__max:
            return True
        else:
            return False

    def get_character(self, index):
        return self.__list_of_characters[index]

    def get_character_list(self):
        return self.__list_of_characters

    def get_index(self, character):
        for index in range(len(self.__list_of_characters)):
            if self.__list_of_characters[index] == character:
                return index

    def get_fighter(self):
        return self.__fighter

    def get_item_inventory(self, index):
        return self.__inventory[index]

    def set_fighter(self, fighter):
        self.__fighter = fighter
        self.__choose = True

    def remove_fighter(self):
        self.__fighter = None
        self.__choose = False

    def view_stats(self):
        for character in self.__list_of_characters:
            print(character.get_name(), "--> Strength: %s, Agility: %s, Constitution: %s, Health: %s" % character.get_attributes())

    def view_inventory(self):
        if not self.__inventory:
            print("There are no items in your inventory.")
        else:
            for index in range(len(self.__inventory)):
                print(str(index + 1) + ")", self.__inventory[index].get_name(), "-->", self.__inventory[index].get_description())

    def add_item_inventory(self, item):
        self.__inventory.append(item)

    def delete_item_inventory(self, index):
        self.__inventory.pop(index)

    def generate_item(self):
        list_of_items = [("Small health potion.", "Healing", "Small potion that restores 25 health points.", "Small"),
                         ("Small health potion.", "Healing", "Small potion that restores 25 health points.", "Small"),
                         ("Large health potion.", "Healing", "Large potion that restores 50 health points.", "Large"),
                         ("Large health potion.", "Healing", "Large potion that restores 50 health points.", "Large"),
                         ("Attack x2", "Attack", "Brew that temporarily doubles the fighter's attack.", "Small"),
                         ("Attack x5", "Attack", "Super powerful infusion that quintuples the fighter's attack temporarily.", "Large"),
                         ("Little bottle of experience", "Leveling", "Increase 15 experience points.", "Small"),
                         ("Barrel of experience.", "Leveling", "Barrel that increases 50 experience points.", "Large")]
        index = randint(0, 7)
        item = Items(list_of_items[index][0], list_of_items[index][1], list_of_items[index][2], list_of_items[index][3])
        self.add_item_inventory(item)
        print("You have a new item in your inventory!")

    def use_item(self):
        if self.__inventory:
            print("Choose item to use:")
            lenght = len(self.__inventory)
            lenght2 = len(self.__list_of_characters)
            self.view_inventory()
            op = check_input(1, lenght)
            item = self.get_item_inventory(op-1)
            print("Choose the character you are going to give the item to.")
            self.view_character_list()
            op2 = check_input(1, lenght2)
            character = self.get_character(op2-1)
            item.use(character)
            self.delete_item_inventory(op-1)
        else:
            print("You don't have any items in your inventory.")


def check_input(minimum, maximum):
    while True:
        value = int(input("Choose an option: "))
        if minimum <= value <= maximum:
            return value
        else:
            print("Input error.")