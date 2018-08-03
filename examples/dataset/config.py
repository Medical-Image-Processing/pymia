import pymia.config.configuration as pymia_cfg


class Configuration(pymia_cfg.ConfigurationBase):
    VERSION = 1
    TYPE = ''

    @classmethod
    def version(cls) -> int:
        return cls.VERSION

    @classmethod
    def type(cls) -> str:
        return cls.TYPE

    def __init__(self):
        self.database_file = 'out/test/test.h5'

        self.batch_size_training = 10
        self.batch_size_testing = 10
        self.epochs = 20


def load(path: str, config_cls):
    """Loads a configuration file.

    Args:
        path (str): The path to the configuration file.
        config_cls (class): The configuration class (not an instance).

    Returns:
        (config_cls): The configuration.
    """

    return pymia_cfg.JSONConfigurationParser.load(path, config_cls)
