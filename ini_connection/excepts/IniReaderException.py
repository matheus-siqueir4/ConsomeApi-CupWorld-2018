class IniReaderException():

    def __init__(self, typeError, message):
        self.typeError = typeError
        self.message = message

    def buildErrorIniReader(self):
        return f"""
        TypeError: {self.typeError.__name__}
        Message: {self.message}
        """
    
    def UnexpectedError(self):
        message = f"Um erro fatal ocorreu: {self.buildErrorIniReader()}"
        print(message)
        exit()