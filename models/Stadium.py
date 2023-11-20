class Stadium():
    
    def __init__(self, key, name):
        self._key = key
        self._name = name
    
    def __str__(self) -> str:
        return f"""
        Key: {self._key}
        Name: {self._name}
        """
    @property
    def name(self) -> str:
        return self._name

    def key(self) -> str:
        return self._key