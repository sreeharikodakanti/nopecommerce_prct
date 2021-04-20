import configparser
config = configparser.RawConfigParser()
config.read(".//configuration/config.ini")


class readconfigs:
    @staticmethod
    def geturl():
        url = config.get('common file','Base_url')
        return url
    @staticmethod
    def getusername():
        username = config.get('common file','username')
        return username
    @staticmethod
    def getpassword():
        password = config.get('common file','password')
        return password