from crystal_engine.client.ConfigurationManager import ConfigurationManager

def screen_size():
    return ConfigurationManager.get("screensize")

class Width:
    @staticmethod
    def half():
        return screen_size()[0] / 2

    @staticmethod
    def quarter():
        return screen_size()[0] / 4

class Height:
    @staticmethod
    def half():
        return screen_size()[1] / 2

    @staticmethod
    def quarter():
        return screen_size()[1] / 4