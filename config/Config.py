import ConfigParser


class Config:
    config_file = 'config.ini'

    def __init__(self):
        config = ConfigParser.ConfigParser().read(self.config_file)

    def get(self, section, key):
        return self.config.get(section, key)
