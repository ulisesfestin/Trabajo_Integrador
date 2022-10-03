from GSC_Constants import *


class Controller:
    def __init__(self, max_of_characters):
        self.__list_of_characters = []
        self.__dead_list = []
        self.__fighter = None
        self.__choose = False
        self.__max = max_of_characters

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
        for element in self.__list_of_characters:
            print(element.get_attributes())