from data_processing.DataManipulation import DataManipulation
from models.Match import Match
from models.Goal import Goal

class DataPrinter:

    @staticmethod
    def searchGamesPrinter(choice: int):
        matches = DataManipulation.searchGames(tipo=choice)
        DataPrinter._percorreMatches(matches)

    @staticmethod
    def searchGroupStagePrinter(choice):
        matches = DataManipulation.searchGroupStage(stage=choice)
        DataPrinter._percorreMatches(matches)
    
    @staticmethod
    def searchSelectionPrinter(choice: str):
        matchSelection = DataManipulation.searchSelection(selection=choice)
        DataPrinter._percorreMatches(matchSelection)

    @staticmethod
    def goalsPlayerPrinter(choice: str):
        goal = DataManipulation.golsPlayer(choice)
        DataPrinter._percorreGoals(goal)

    @staticmethod
    def searchStadiumPrinter(choice: str):
        result = DataManipulation.searchStadium(choice)
        DataPrinter._percorreMatches(result)

    @staticmethod
    def searchCityPrinter(choice: str):
        result = DataManipulation.searchCity(choice)
        DataPrinter._percorreMatches(result)

    @staticmethod
    def _percorreMatches(array: list[Match]):
        
        if array:
            for match in array:
                print(match.teamHomeVsTeamAway())

        else:
            print("Nenhuma partida encontrada: Verifique se foi digitado corretamente!")

    def _percorreGoals(obj: Goal):
        if obj:
            print(obj)
        else:
            print("Nenhum Jogador que marcou gols com esse nome foi encontrado")