class ConfigurationManager:
    @staticmethod
    def set(key, value):
        setattr(ConfigurationManager, key, value)

    @staticmethod
    def get(key):
        return getattr(ConfigurationManager, key)