import random
import time

from Character import Character
from GSC_Constants import *


class Human(Character):
    def __init__(self, name, age, strength, agility, constitution, type):
        super().__init__(name, age, strength, agility, constitution, type)
        self.__strength = strength + TYPE_ADVANTAGE
        self.__agility = agility
        self.__constitution = constitution
        self.__health = BASE_HEALTH + (self.__constitution * HEALTH_MULTIPLIER)

    def get_attributes(self):
        return self.__strength, self.__agility, self.__constitution, self.__health

    def check_health(self):
        if self.__health > 0:
            return True
        else:
            return False

    def set_health(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            self.set_is_live(False)

    def get_health(self):
        return self.__health

    def attack(self, target):
        print(self.get_name(), "is attacking", target.get_name())
        print("Rolling dice...")
        time.sleep(0)
        dice = random.randint(1, 6) + random.randint(1, 6)
        print("You got a %s!" % dice)
        if dice in FIRST_GROUP:
            target.set_health(self.__strength * FIRST_GROUP_DAMAGE)
        elif dice in SECOND_GROUP:
            target.set_health(self.__strength * SECOND_GROUP_DAMAGE)
        elif dice in THIRD_GROUP:
            target.set_health(self.__strength * THIRD_GROUP_DAMAGE)
        else:
            target.set_health(self.__strength * CRITICAL_DAMAGE)
            print("Critical hit!")
