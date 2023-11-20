from .DataPrinter import DataPrinter
from .UserInputHandler import userInput

class Tela:

    def __init__(self):
        
        self._menuPrincipal = """
            1. Jogos realizados por determinado grupo ou fase
            2. Pesquisar jogos de uma seleção
            3. Jogos com vitória do visitante
            4. Jogos que terminaram empatados
            5. Jogos que tiveram vitória do mandante
            6. Jogos que foram realizados em determinado estádio
            7. Jogos que foram realizados em determinada cidade
            8. Pesquisar quantidade de gols realizados por um jogador
            0. Sair
            """

        self._faseOrGroup = """
            1. Pesquisar por Grupo.
            2. Pesquisar por eliminatórias
            0. Voltar
            """

        self._group = """
            1. Group A
            2. Group B
            3. Group C
            4. Group D
            5. Group E
            6. Group F
            7. Group G
            8. Group H
            0. Voltar
            """
        
        self._fase = """
            1. Round of 16
            2. Quarter-finals
            3. Semi-finals
            4. Final
            0. Voltar
            """
        
        self._situation = """
        1. Vitórias do time da casa
        2. Vitórias do time de fora
        3. Empates
        0. Voltar
        """

    @property
    def menuPrincipal(self):
        return self._menuPrincipal

    @property
    def faseOrGroup(self):
        return self._faseOrGroup

    @property
    def group(self):
        return self._group    

    @property
    def fase(self):
        return self._fase
    

    def FirstMenu(self):
        flag = True

        while (flag):
            
            print(self.menuPrincipal)
            choice = userInput.userChoice(0, 8)
    
            if choice == 0:
                flag = False

            elif choice == 1:
                self.groupOrFaseList()
            
            elif choice == 2:
               self.searchSelectionInterface() 
            
            elif choice == 3:
                self.matches(3)

            elif choice == 4:
                self.matches(1)
            
            elif choice == 5:
                self.matches(2)
            
            elif choice == 6:
                self.printSearchStadium()
            
            elif choice == 7:
                self.printSearchCity()

            elif choice == 8:
                self.printSearchPlayerGoal()

    def printSearchPlayerGoal(self):
        choice = input("Qual nome do Jogador? ")
        DataPrinter.goalsPlayerPrinter(choice=choice)
        input("Aperte qualquer tecla para voltar ao menu principal: ")

    def printSearchStadium(self):
        choice = input("Qual estádio deseja buscar? ")
        DataPrinter.searchStadiumPrinter(choice=choice)
        input("Aperte qualquer tecla para voltar ao menu principal: ")


    def printSearchCity(self):
        choice = input("Qual Cidade deseja buscar? ")
        DataPrinter.searchStadiumPrinter(choice=choice)
        input("Aperte qualquer tecla para voltar ao menu principal: ")

    def matches(self, choice):
        DataPrinter.searchGamesPrinter(choice)
        input("Aperte qualquer tecla para voltar ao menu principal: ")

    def searchSelectionInterface(self):
        choice = input("Qual seleção deseja buscar? ")
        DataPrinter.searchSelectionPrinter(choice=choice)
        input("Aperte qualquer tecla para voltar ao menu principal: ")

    def groupOrFaseList(self):
        flag = True
        print(self.faseOrGroup)
        choice = userInput.userChoice(0, 3)

        while(flag):
            
            if choice == 0:
                flag = False
        
            elif choice == 1:
                print(self.group)
                choice = userInput.userChoice(0, 8)
                group = userInput.choiceGroup(choice)
                DataPrinter.searchGroupStagePrinter(group)
                input("Aperte qualquer tecla para voltar ao menu principal: ")
                flag = False

            elif choice == 2:
                print(self.fase)
                choice = userInput.userChoice(0, 4)
                fase = userInput.choiceFase(choice)
                DataPrinter.searchGroupStagePrinter(fase)
                input("Aperte qualquer tecla para voltar ao menu principal: ")
                flag = False