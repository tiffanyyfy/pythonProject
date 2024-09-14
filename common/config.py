import configparser


class Config:
    __configFile = f"D:\pywork\pythonProject\data\config.ini"

    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read(Config.__configFile)
        self.__server = conf.get("database", "server")
        self.__username = conf.get("database", "username")
        self.__password = conf.get("database", "password")
        self.__port = conf.get("database", "port")
        self.__dbname = conf.get("database", "dbname")

    @property
    def get_server(self):
        return self.__server

    @property
    def get_username(self):
        return self.__username

    @property
    def get_password(self):
        return self.__password

    @property
    def get_port(self):
        return self.__port

    @property
    def get_dbname(self):
        return self.__dbname


config = Config()
