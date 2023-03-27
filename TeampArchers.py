from ArcherPlayer import ArcherPlayer

"""
    teamScore: un atributo de clase que representa la puntuación del equipo.
"""
class Team(list):
    teamScore = 0
    name = ""

    """
        init(): un constructor que inicializa un equipo con cinco instancias de la clase "ArcherPlayer".
    """
    def __init__(self, name):
        self.name = name
        self.team = [ArcherPlayer(), ArcherPlayer(), ArcherPlayer(), ArcherPlayer(), ArcherPlayer()]

    """
        updateTeamScore(score): un método que actualiza la puntuación del equipo agregando el valor de "score".
    """
    def updateTeamScore(self, score):
        self.teamScore += score

    """
        iter(): un método que devuelve un iterador sobre los arqueros del equipo.
    """
    def __iter__(self):
        self.index = 0
        return self

    """ 
        next(): un método que devuelve el siguiente arquero del equipo en cada
        llamada hasta que se alcanza el final de la lista, momento en que se genera una excepción StopIteration.
    """
    def __next__(self):
        if self.index >= len(self.team):
            raise StopIteration
        result = self.team[self.index]
        self.index += 1
        return result
