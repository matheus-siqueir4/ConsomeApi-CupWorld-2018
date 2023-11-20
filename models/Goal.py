class Goal:

    def __init__(self, jogador) -> None:
        self._name = jogador
        self._goals = 1
    
    def __str__(self) -> str:
        return f"""
        Player: {self._name}
        Total goals: {self._goals} 
        """

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Goal):
            return self.name == other.name
        return False
    
    @property
    def name(self):
        return self._name
    
    def addGoal(self):
        self._goals += 1