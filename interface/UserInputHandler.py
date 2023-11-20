class UserInputHandler():
        
    def userChoice(self, start, end):

        while True:
            choice = input("Escolha uma dentre as opções numéricas: ")
            
            try:
                choiceInt = int(choice)
                
                if not (start <= choiceInt <= end):
                    print("Escolha um número dentro do limite de opções")
                    continue
                return choiceInt

            except ValueError:
                print("Escolha um número inteiro")
 
    
    def choiceGroup(self, choice):

        arrayGroup = ["Group A", "Group B", "Group C", "Group D", 
                    "Group E", "Group F", "Group G", "Group H"]
        
        for index, group in enumerate(arrayGroup, start=1):
            
            if choice == index:
                return group

    def choiceFase(self, choice):

        arrayFase = ["Round of 16", "Quarter-finals", "Semi-finals", "Final"]

        for index, fase in enumerate(arrayFase, start=1):
            
            if choice == index:
                return fase 

userInput = UserInputHandler()