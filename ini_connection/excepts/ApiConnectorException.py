class ApiConnectorException():

    def __init__(self, typeError, message, status = None):
        self.typeError = typeError
        self.message = message
        self.status = status

    def UnexpectedErrorResponseAPI(self):
        message = f"Um erro fatal ocorreu: {self.buildErrorResponseAPI()}"
        print(message)
        exit()

    def buildErrorResponseAPI(self):
        return f"""
        TypeError: {self.typeError.__name__}
        Status: {self.status}
        Message: {self.message}
        """