from GSC_Constants import *

name = str(input(INPUT_NAME))
age = int(input(INPUT_AGE))



def Distribute_score():
    global strength, agility, constitution
    strength = 0
    agility = 0
    constitution = 0
    score = 15
    while score > 0:
        print(INPUT_SCORE1, score, INPUT_SCORE2)
        strength = int(input(INPUT_STRENGTH))
        score = score-strength  
        if score < 0:
            Distribute_score()
        else:
            pass
        print(INPUT_SCORE1, score , INPUT_SCORE2)
        agility = int(input(INPUT_AGILITY))
        score = score-agility
        if score < 0:
            Distribute_score()
        else:
            pass
        print(INPUT_SCORE1, score , INPUT_SCORE2)
        constitution = int(input(INPUT_CONSTITUTION))
        score = score-constitution
        if score < 0:
            Distribute_score()
        else:
            pass
Distribute_score()
type = str(input(INPUT_TYPE))


print(name," ", age," ", strength," ", agility," ", constitution)

