from .Data import Data

from ini_connection.APIConnector import APIConnector

from models.Goal import Goal
from models.Team import Team
from models.Match import Match
from models.Stadium import Stadium

class LoadingData:

    # Cria uma instância com o arquivo ini desejado para carregamento de dados
    apiConn: APIConnector = APIConnector('info', 'url', './config/api_url.ini')

    connJSON: dict = apiConn.loadData() # Carrega os dados da API

    @staticmethod
    def AllGames() -> None:
        """
        Carrega todos os jogos em memória.
        """

        for match in LoadingData.connJSON["rounds"]:
            
            matchDay: str = match["name"]

            for game in match["matches"]:
                    
                teamHome = Team(game["team1"]["name"], game["team1"]["code"])
                teamAway = Team(game["team2"]["name"], game["team2"]["code"])
                stadium = Stadium(game["stadium"]["key"], game["stadium"]["name"])
                
                # Verifica se a chave "group" existe no json
                level = game.get("group", matchDay)
                    
                match = Match(teamHome=teamHome,
                    teamAway=teamAway,
                    scoreHome=game["score1"], 
                    scoreAway=game["score2"], 
                    stadium=stadium, 
                    city=game["city"], 
                    level=level)
                
                Data.storeMatches(match) # Armazena os objetos em uma Lista dentro da class Data

    
    @staticmethod
    def Allgoals() -> None:
        """
        Carrega todos os gols realizados em todas as partidas
        """
        listaObjGoals: list[Goal] = [] # Objetos que já foram inseridos em Data
        
        for match in LoadingData.connJSON["rounds"]:
            for game in match["matches"]: 
                
                allGoals: list[str] = game["goals1"] + game["goals2"] # Coloca todos os gols da partida em uma só lista
                 
                for goal in allGoals:

                    objGoal = Goal(goal["name"]) # Cria um objeto de Goal
    
                    if (objGoal in listaObjGoals): # Verifica se o objeto já foi inserido
                        existingObjGoal = listaObjGoals[listaObjGoals.index(objGoal)] # Captura o obj
                        existingObjGoal.addGoal() # Adiciona mais um gol
                        continue
                    
                    else:
                        listaObjGoals.append(objGoal)
                        Data.storeGoals(objGoal)