class Items:
    def __init__(self, name, type, description, size):
        self.__name = name
        self.__type = type
        self.__description = description
        self.__size = size

    def use(self, objective):
        if self.__type == "Healing":
            if self.__size == "Small":
                objective.healing(25)
            elif self.__size == "Large":
                pass

        pass


"""item1 = Items("pocion pequeña de vida", "pequeño", "vida", "esta pocion aumentara un poco tu vida")

item2 = Items("pocion pequeña de fuerza","pequeño","fuerza","esta pocion aumentara un poco tu fuerza")

item3 = Items("pocion pequeña de experiencia","pequeño","experiencia","esta pocion aumentara un poco tu experiencia")

item4 = Items("pocion grande de vida","grande","vida","esta pocion aumentara mucho tu vida")

item5 = Items("pocion grande de fuerza","grande","fuerza","esta pocion aumentara mucho tu fueza")

item6 = Items("pocion grande de experiencia","grande","experiencia","esta pocion aumentara mucho tu experiencia")"""