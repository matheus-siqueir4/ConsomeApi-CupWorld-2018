from models.Match import Match
from models.Goal import Goal

class Data:

    modelsMatches: list[Match] =  []

    modelsGoals: list[Goal] = []

    @classmethod
    def storeMatches(cls, obj: Match):
        cls.modelsMatches.append(obj)
    
    @classmethod
    def storeGoals(cls, obj: Goal):
        cls.modelsGoals.append(obj)