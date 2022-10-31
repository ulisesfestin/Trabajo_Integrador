from GSC_Constants import *


class Items:
    def __init__(self, name, type, description, size):
        self.__name = name
        self.__type = type
        self.__description = description
        self.__size = size

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_description(self):
        return self.__description

    def get_size(self):
        return self.__size

    def use(self, objective):
        if self.__type == "Healing":
            if self.__size == "Small":
                objective.healing(SMALL_HEALTH_POTION)
            elif self.__size == "Large":
                objective.healing(LARGE_HEALTH_POTION)
        elif self.__type == "Attack":
            if self.__size == "Small":
                objective.multiply_damage(ATTACK_X2)
            elif self.__size == "Large":
                objective.multiply_damage(ATTACK_X5)
        elif self.__type == "Leveling":
            if self.__size == "Small":
                objective.raise_xp(SMALL_BOTTLE_OF_XP)
            elif self.__size == "Large":
                objective.raise_xp(BARREL_OF_XP)
