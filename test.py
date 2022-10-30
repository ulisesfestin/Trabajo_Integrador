from GSC_Constants import *
#tamaño: grande, chico ; mejora: vida, fuerza, experiencia.
class Items:
    def __init__(self, nombre, tamaño, mejora, descripcion):
        self.nombre = nombre
        self.tamaño1 = tamaño
        self.mejora1 = mejora
        self.descripcion = descripcion


item1 = Items("pocion pequeña de vida", "pequeño", "vida", "esta pocion aumentara un poco tu vida")

item2 = Items("pocion pequeña de fuerza","pequeño","fuerza","esta pocion aumentara un poco tu fuerza")

item3 = Items("pocion pequeña de experiencia","pequeño","experiencia","esta pocion aumentara un poco tu experiencia")

item4 = Items("pocion grande de vida","grande","vida","esta pocion aumentara mucho tu vida")

item5 = Items("pocion grande de fuerza","grande","fuerza","esta pocion aumentara mucho tu fueza")

item6 = Items("pocion grande de experiencia","grande","experiencia","esta pocion aumentara mucho tu experiencia")
