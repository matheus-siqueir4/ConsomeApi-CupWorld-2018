class Match:

    def __init__(self, teamHome, teamAway, scoreHome, scoreAway, stadium, city, level) -> None:
        self._teamHome = teamHome
        self._teamAway = teamAway
        self._scoreHome = scoreHome
        self._scoreAway = scoreAway
        self._stadium = stadium
        self._level = level
        self._city = city

    def __str__(self) -> str:
        return f"""
        Team Home: {self._teamHome}
        Team Visiting: {self._teamAway}
        Stadium: {self._stadium}
        Level: {self._level}
        City: {self._city}
        """
        
    @property
    def scoreHome(self) -> int:
        return self._scoreHome

    @property
    def scoreAway(self) -> int:
        return self._scoreAway
    
    @property
    def teamHome(self) -> str:
        return self._teamHome
    
    @property
    def teamAway(self) -> str:
        return self._teamAway

    @property
    def level(self) -> str:
        return self._level 

    @property
    def city(self):
        return self._city
    
    @property
    def stadium(self):
        return self._stadium

    def teamHomeVsTeamAway(self) -> str:
        return f"{self._level}:\n {self._teamHome} vs {self._teamAway}"
