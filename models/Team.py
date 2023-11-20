class Team():
    
    def __init__(self, name, code):
        self._name = name
        self._code = code

    def __str__(self) -> str:
        return f"""
        Name: {self._name}
        Code: {self._code}
        """
  
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    658349379
