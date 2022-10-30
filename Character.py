from GSC_Constants import *


class Character:
    def __init__(self, name, age, strength, agility, constitution, type):
        self.__name = name if self.check_validate_name(name) else EMPTY_STR
        self.__age = age if self.check_validate_age(age) else EMPTY_INT
        self.__strength = strength if self.check_validate_atributes(strength, agility, constitution, type) else EMPTY_INT
        self.__agility = agility if self.check_validate_atributes(strength, agility, constitution, type) else EMPTY_INT
        self.__constitution = constitution if self.check_validate_atributes(strength, agility, constitution, type) else EMPTY_INT
        self.__type = type
        self.__live = True

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_type(self):
        return self.__type

    def get_is_live(self):
        return self.__live

    def set_is_live(self, status: bool):
        self.__live = status

    def set_age(self, age):
        self.__age = age if self.check_validate_age(age) else EMPTY_INT

    def set_name(self, name):
        self.__name = name if self.check_validate_name(name) else EMPTY_STR

    def check_validate_age(self, age):
        if age > AGE_PARAMETER:
            return True
        else:
            print(ERROR_AGE)
            return False

    def check_validate_name(self, name):
        if type(name) is str and not any(char.isdigit() for char in name):
            return True
        else:
            print(ERROR_NAME)
            return False

    def check_validate_atributes(self, strength, agility, constitution, type):
        if type != ENEMY_TYPE:
            if strength + agility + constitution == ATTRIBUTES_PARAMETER_CHAR:
                return True
            else:
                return False
        else:
            if strength + agility + constitution == ATTRIBUTES_PARAMETER_ENEMY:
                return True
            else:
                return False

    def move(self):
        print(CHARACTER_MOVING)

    def __str__(self):
        string = self.__name + " (" + self.__type + ")"
        return string


