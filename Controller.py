from GSC_Constants import *


class Controller:
    def __init__(self, max_of_characters):
        self.__list_of_characters = []
        self.__dead_list = []
        self.__fighter = None
        self.__choose = False
        self.__max = max_of_characters
        self.__inventory = [("Small life potion.", "Healing", "Small potion that restores 25 health points.", "Small"),
                            ("Large health potion.", "Healing", "Large potion that restores 50 health points.", "Large"),
                            ("Attack x2", "Attack", "Brew that temporarily doubles the fighter's attack.", "Small"),
                            ("Attack x5", "Attack", "Super powerful infusion that quintuples the fighter's attack temporarily.", "Larger"),
                            ("Little bottle of experience", "Leveling", "Increase 15 experience points.", "Small"),
                            ("Barrel of experience.", "Leveling", "Barrel that increases 50 experience points.", "Large")]

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

    def get_index(self, character):
        for index in range(len(self.__list_of_characters)):
            if self.__list_of_characters[index] == character:
                return index

    def get_fighter(self):
        return self.__fighter

    def set_fighter(self, fighter):
        self.__fighter = fighter
        self.__choose = True

    def view_stats(self):
        for character in self.__list_of_characters:
            print(character.get_name(), "--> Strength: %s, Agility: %s, Constitution: %s, Health: %s, level: %s" % character.get_attributes())

    def view_inventory(self):
        for index in range(len(self.__inventory)):
            print(str(index + 1) + ")", self.__inventory[index].get_name(), "-->", self.__inventory[index].get_description())

    def add_item_inventory(self, item):
        self.__inventory.append(item)

    def generate_item(self):
        pass
