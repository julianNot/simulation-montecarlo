from colorama import init, Fore, Back, Style
from prettytable import PrettyTable
from TeampArchers import Team
import random
import matplotlib.pyplot as plt

"""
    "teamOne" y "teamTwo", que son instancias de la clase "Team". Este método inicia la biblioteca "colorama"
    usando el método "init" y luego ejecuta un bucle "while" que se ejecuta hasta que se juegan 55 partidos.

    Dentro del bucle "while", el método "resetEndurance" se llama en ambos equipos para restablecer su resistencia
    antes de cada ronda del partido. Luego, el método "initRounds" se llama para simular una ronda de juego entre ambos equipos.

    Al final del juego, el puntaje de ambos equipos se imprime usando la biblioteca "colorama" 
"""
def initGame(teamOne, teamTwo):
    init()
    table = PrettyTable()
    table.field_names = [Fore.RED+"Team", Fore.GREEN+"Score"]
    games = 1000
    while games > 0:
        resetEndurance(teamOne, teamTwo)
        initRounds(teamOne, teamTwo)
        games -= 1
    table.add_row([teamOne.name, teamOne.teamScore])
    table.add_row([teamTwo.name, teamTwo.teamScore])
    showTableGenderScore(teamOne, 'Equipo 1')
    showTableGenderScore(teamTwo, 'Equipo 2')
    showWinTeam(teamOne, teamTwo)
    print(table)

"""
    Dentro del bucle "while", el método "takeShot" se llama en "Archer" para simular un disparo.
    La puntuación del jugador se incrementa con el resultado del método "takeShot", y la resistencia
    del jugador disminuye en 5.

    Después de que se completa el bucle "while", la tabla de resultados se actualiza con la puntuación
    final del jugador y se imprime. Además, se actualiza la resistencia y la puntuación del jugador "Archer"
    y la puntuación del equipo "team".

    Por último, hay una sentencia condicional que reduce la resistencia de "Archer" en 2 con una probabilidad
    del 50%, o en 1 con una probabilidad del 50%
"""
def shootingPlayers(Archer, team):
    table = PrettyTable()
    endurance = Archer.endurance
    table.field_names = [Fore.RED+"Endurance", Fore.GREEN+"Score", "Gender"]
    playerScore = 0
    while endurance > 5:
        playerScore += takeShot(Archer)
        endurance -= 5
    table.add_row([Archer.endurance, playerScore, "Mujer" if Archer.gender == 1 else "Hombre"])
    if random.random() < 0.5:
        Archer.endurance -= 2
    else:
        Archer.endurance -= 1
    Archer.setIndividualScore(playerScore)
    team.updateTeamScore(playerScore)
    print(table)

""" 
    Primero, se genera un número aleatorio "shot" con el método "random.random()".
    A continuación, se verifica el género del jugador "archer". Si es masculino (0),
    las probabilidades de obtener una puntuación de 10, 9, 8 o 0 son 20%, 33%, 40% y 7%, respectivamente.
    Si es femenino (1), las probabilidades de obtener una puntuación de 10, 9, 8 o 0 son 30%, 38%, 27% y 5%, respectivamente.

    Finalmente, se devuelve la puntuación correspondiente según la precisión del disparo.
"""
def takeShot(archer):
    shot = random.random()
    if archer.gender == 0:
        if shot <= 0.2:
            return 10
        elif 0.2 < shot <= 0.53:
            return 9
        elif 0.53 < shot <= 0.93:
            return 8
        else:
            return 0
    elif archer.gender == 1:
        if shot <= 0.3:
            return 10
        elif 0.3 < shot <= 0.68:
            return 9
        elif 0.68 < shot <= 0.95:
            return 8
        else:
            return 0

"""
    se establece la variable "cycle" en 10. Luego, se inicia un bucle "while"
    que se ejecuta hasta que "cycle" sea menor o igual a 0. Dentro del bucle,
    se ejecuta un bucle "for" para cada jugador de los equipos "teamOne" y "teamTwo", respectivamente.

    Para cada jugador, se llama al método "shootingPlayers" para simular una ronda de tiro,
    y se le pasan como argumentos el jugador y su respectivo equipo.
"""        
def initRounds(teamOne, teamTwo):
    cycle = 10
    while cycle > 0:
        for archer in teamOne:
            shootingPlayers(archer, teamOne)
            print("==========Team One==========")
        for archer in teamTwo:
            shootingPlayers(archer, teamTwo)
            print("==========Team Two==========")
        extraShotDraw(teamOne), extraShotDraw(teamTwo)
        cycle -= 1

"""
    se ejecuta un bucle "for" para cada arquero en el equipo "team_1". Para cada arquero, 
    se llama al método "resetEndurance" de la clase "Player", que reinicia la resistencia del arquero a su valor máximo.

    Luego, se ejecuta otro bucle "for" para cada arquero en el equipo "team_2", 
    y se repite el proceso anterior para cada arquero.
""" 
def resetEndurance(team_1, team_2):
    for archer in team_1:
        archer.resetEndurance()
    for archer in team_2:
        archer.resetEndurance()

"""
    se ejecuta un bucle "for" para cada arquero en el equipo. Para cada arquero,
    se compara su atributo "luck" con la variable "max_luck". Si el atributo "luck" del arquero es mayor que "max_luck",
    se actualiza "max_luck" y se asigna el arquero a "luckiest_archer".

    Después de encontrar al arquero más afortunado, se llama al método "updateTeamScore" de la clase "Team" con un parámetro,
    que es el resultado de la función "takeShot" para el "luckiest_archer". Esto significa que el arquero más afortunado tiene
    la oportunidad de realizar un tiro adicional para su equipo.
"""
def extraShotDraw(team):
    maxLuck = 0
    luckiestArcher = None
    for archer in team:
        if archer.luck > maxLuck:
            maxLuck = archer.luck
            luckiestArcher = archer
    team.updateTeamScore(takeShot(luckiestArcher))

def showTableGenderScore(archers, teamName):
    score_men = []
    score_womens = []
    total_womens = 0
    total_mens = 0

    for archer in archers:
        if archer.gender == 1:
            score_men.append(archer.individual_score)
            total_mens += 1
        else:
            score_womens.append(archer.individual_score)
            total_womens += 1

        categories = [f"Mujeres ({total_womens})", f"Hombres ({total_mens})"]

        if len(score_womens) > 0:
            average_womens = sum(score_womens) / len(score_womens)
        else:
            average_womens = 0

        if len(score_men) > 0:
            average_mens = sum(score_men) / len(score_men)
        else:
            average_mens = 0 

        heights = [average_womens, average_mens]

    plt.figure(figsize=(8, 6))
    plt.bar(categories, heights, color=['pink', 'blue'])
    plt.title(f'Puntuación Promedio por Género {teamName}')
    plt.xlabel('Género')
    plt.ylabel('Puntuación Promedio')
    plt.show()

def showWinTeam(team1, team2):
    plt.bar([team1.name, team2.name], [team1.teamScore, team2.teamScore], color=['red', 'blue'])
    plt.title('Puntaje de Equipos')
    plt.xlabel('Equipos')
    plt.ylabel('Puntaje')

    womens_team1 = sum(1 for archer in team1 if archer.gender == 0)
    mens_team1 = sum(1 for archer in team1 if archer.gender == 1)
    womens_team2 = sum(1 for archer in team2 if archer.gender == 0)
    mens_team2 = sum(1 for archer in team2 if archer.gender == 1)

    print(f"{team1.name}: Mujeres: {womens_team1}, Hombres: {mens_team1}")
    print(f"{team2.name}: Mujeres: {womens_team2}, Hombres: {mens_team2}")

    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))

    plt.tight_layout()
    plt.show()
    

teamOneInit = Team("Team 1")
teamTwoInit = Team("Team 2")

initGame(teamOneInit, teamTwoInit)
