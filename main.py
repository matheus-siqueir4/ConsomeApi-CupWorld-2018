from data_processing.LoadingData import LoadingData
from interface.Tela import Tela

tela = Tela()

if __name__ == "__main__":
    LoadingData.AllGames()
    LoadingData.Allgoals()
    tela.FirstMenu()