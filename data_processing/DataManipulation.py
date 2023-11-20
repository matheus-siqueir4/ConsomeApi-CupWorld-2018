from .Data import Data

from models.Match import Match
from models.Goal import Goal

class DataManipulation:
    
    @staticmethod
    def searchGames(tipo) -> list[Match]:
        """
        Quais jogos tiveram vitória do visitante? E quais jogos terminaram
        empatados? Quais jogos tiveram vitória do mandante?
        """
        matches: list[Match] = []

        for obj in Data.modelsMatches:
            scoreHome = getattr(obj, 'scoreHome', None)
            scoreAway = getattr(obj, 'scoreAway', None)

            if (tipo == 1) and (scoreHome == scoreAway): # Empates
                matches.append(obj)

            elif (tipo == 2) and (scoreHome > scoreAway): # Vitoria Mandante
                matches.append(obj)
            
            elif (tipo == 3) and (scoreAway < scoreHome): # Vitoria Visitante
                matches.append(obj)
            
            elif tipo > 3 or tipo < 0:
                return None
        
        return matches

    @staticmethod
    def searchGroupStage(stage) -> list[Match]:
        """
        Quais jogos foram realizados em determinado grupo ou fase (oitavas,
        quartas, semi e final)?
        """
        matches: list[Match] = []

        for obj in Data.modelsMatches:
            result = getattr(obj, 'level', None)

            if result == stage:
                matches.append(obj)

        return matches

    @staticmethod
    def searchSelection(selection) -> list[Match]:
        """
        Quais jogos foram realizados por determinada seleção?
        """
        matches: list[Match] = []
        for obj in Data.modelsMatches:
            teamHome = getattr(obj, 'teamHome', None)
            teamAway = getattr(obj, 'teamAway', None)
            
            if selection in (teamHome.code, teamAway.code, teamHome.name, teamAway.name):
                matches.append(obj)
        return matches

    def golsPlayer(player) -> Goal:
        """
        Quantos gols foram feitos por determinado jogador?
        """
        for obj in Data.modelsGoals:
            name = getattr(obj, 'name', None)

            if player == name:
                return obj

    @staticmethod
    def searchStadium(search) -> list[Match]:
        """
        Quais jogos foram realizados em determinada cidade
        Quais jogos foram realizados em determinado estádio
        """
        matches: list[Match] = []

        for obj in Data.modelsMatches:
            result: Match = getattr(obj, 'stadium', None)
            
            if search  == result.name:
                matches.append(obj)
        return matches

    def searchCity(search) -> list[Match]:
        """
        Quais jogos foram realizados em determinada cidade
        Quais jogos foram realizados em determinado estádio
        """
        matches: list[Match] = []

        for obj in Data.modelsMatches:
            result = getattr(obj, 'city', None)
            
            if search == result:
                matches.append(obj)
        return matches