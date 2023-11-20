import configparser

from .excepts.IniReaderException import IniReaderException

class iniReader:

    def __init__(self, section, option, filepath):
        self.section = section
        self.option = option
        self.filepath = filepath
        self.config = configparser.ConfigParser()

    def initialize_connection(self) -> str:
        URL: str = self._loadIniFile()
        return URL

    def _loadIniFile(self) -> str:
        iniException: object = None
        fileRead: list[str] = self.config.read(self.filepath)
        
        if (fileRead):
            
            try:
                URL: str = self.config.get(self.section, self.option)
                return URL
            
            except (configparser.NoOptionError, configparser.NoSectionError) as e:
                iniException = IniReaderException(typeError=type(e), message=e.message)

            except Exception as e:
                iniException = IniReaderException(typeError=type(e), message="Unknow Error")
                
        else:
            iniException = IniReaderException(
                typeError=FileNotFoundError, 
                message="Please check the path and file name and try again.")

        if iniException:
            iniException.UnexpectedError()