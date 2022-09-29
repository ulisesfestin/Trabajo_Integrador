from Character import Character
from GSC_Constants import *


class Orc(Character):
    def __init__(self, name, age, strength, agility, constitution, type):
        super().__init__(name, age, strength, agility, constitution, type)
        self.__strength = strength
        self.__agility = agility
        self.__constitution = constitution + TYPE_ADVANTAGE
        self.__health = BASE_HEALTH + (self.__constitution ** HEALTH_MULTIPLIER) / HEALTH_DIVISOR

    def get_attributes(self):
        return self.__strength, self.__agility, self.__constitution, self.__health

    def check_health(self):
        if self.__health > 0:
            return True
        else:
            return False

    def set_health(self, damage):
        self.__health -= damage
