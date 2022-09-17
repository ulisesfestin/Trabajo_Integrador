from GSC_Constants import *


class Controller:
    def __init__(self):
        self.__list_of_characters = []

    def add_character_list(self, character):
        if self.check_maximum_characters():
            self.__list_of_characters.append(character)
        else:
            return print(ERROR_MAXIMUM_CHARACTERS)

    def view_character_list(self):
        for index in range(len(self.__list_of_characters)):
            print(str(index + 1) + ")", self.__list_of_characters[index].get_name(), "-->", self.__list_of_characters[index].get_type())

    def delete_character_list(self, character):
        self.__list_of_characters.pop(character)
        return print(CHARACTER_DELETED)

    def check_maximum_characters(self):
        if len(self.__list_of_characters) < MAXIMUM_OF_CHARACTERS:
            return True
        else:
            return False
