import requests

from .IniReader import iniReader
from .excepts.ApiConnectorException import ApiConnectorException

class APIConnector:

    def __init__(self, section, option, filepath):
        self.URL = iniReader(section=section, option=option, filepath=filepath).initialize_connection()
        self.data = None

    def _initiateApiConnection(self):
        try:
            response = requests.get(self.URL)
            response.raise_for_status()
            return response
            
        except requests.exceptions.RequestException as e:
            ApiException = ApiConnectorException(type(e), str(e), response.status_code)
            ApiException.UnexpectedErrorResponseAPI()

    def loadData(self) -> dict:
        response = self._initiateApiConnection()
        return response.json()