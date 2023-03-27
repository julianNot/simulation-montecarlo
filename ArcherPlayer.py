import random

""" 
    maxEndurance: esta variable representa la cantidad máxima de resistencia que un arquero puede tener. Su valor inicial es 0.

    gender: esta variable indica el género del arquero, donde 0 representa un arquero masculino y 1 representa un arquero femenino. Su valor inicial es 0.

    individual_score: esta variable representa el puntaje individual de un arquero en una ronda. Su valor inicial es 0.

    endurance: esta variable representa la cantidad de resistencia actual que un arquero tiene en una ronda la iniciar.

    EXP: esta variable representa la cantidad de experiencia que un arquero tiene. Su valor inicial es 10.

    luck: esta variable representa la suerte de un arquero en una ronda. Su valor inicial es 0. puede ir de 1 a 3
"""
class ArcherPlayer:
    maxEndurance = 0
    gender = 0
    individual_score = 0
    endurance = 0
    EXP = 10
    luck = 0
    first_lucky_round = None
    second_lucky_round = None
    last_lucky_round = None
    endurance_bonus_round_activated = None


    """
        num = random.random(): se genera un número aleatorio entre 0 y 1 utilizando el módulo random de Python y se almacena en la variable num.
        if num <= 0.5:: si el número generado es menor o igual a 0.5, el arquero será masculino. Si no, será femenino.

        if num < 0.5:: si el número generado es menor a 0.5, se asigna un valor a endurance que va desde 36 a 45. Si no, se asigna un valor que va desde 25 a 34.

        if num <= 0.3:: si el número generado es menor o igual a 0.3, la propiedad luck del objeto creado se establece en 1. Si no, se verifica si es mayor a 0.3 y menor o igual a 0.66, en cuyo caso se establece en 2. Si no, se establece en 3.

        self.luck = 1 o self.luck = 2 o self.luck = 3: según la condición anterior, se establece la propiedad luck del objeto creado en 1, 2 o 3.
    """
    def __init__(self):
        num = random.random()

        if num <= 0.5:
            self.gender = 0
        elif num > 0.5:
            self.gender = 1

        if num < 0.5:
            self.endurance = 35 + random.randint(1, 10)
        else:
            self.endurance = 35 - random.randint(1, 10)

        if num <= 0.3:
            self.luck = 1
        elif 0.3 < num <= 0.66:
            self.luck = 2
        else:
            self.luck = 3
        self.maxEndurance = self.endurance

    """ 
        recibe un argumento score que representa la puntuación obtenida por un individuo.
        El método aumenta la puntuación individual individual_score de la instancia
        de la clase a la que pertenece, sumando el valor de score al valor previo.
    """
    def setIndividualScore(self, score):
        self.individual_score += score

    """ 
        Este método establece el atributo "endurance" de la instancia actual en el valor del atributo "maxEndurance"
    """
    def resetEndurance(self):
        self.endurance = self.maxEndurance

    """
        actualizar la suerte de un objeto en el juego o la simulación después de ciertos eventos o pasos.
    """
    def recalculateLuck(self):
        self.luck = random.uniform(1, 3)