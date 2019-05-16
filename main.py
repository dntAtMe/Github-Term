import pathlib


class Config:
    """Stores User API Key and app configuration"""

    def __init__(self): pass

    def load(self, json): pass


def create_default_config_file():
    pass


def create_custom_config_file():
    pass


def load_config():
    pass


def write_config(config, file):
    pass


def start():
    answer = ""
    while answer != "Y" and answer != "N":
        if not config_file_exists():
            answer = input("Create default config file? (Y/N)")
        else:
            break
    if answer == "Y":
        create_default_config_file()
    else:
        create_custom_config_file()
    read_config_file()


def config_file_exists(path=pathlib.Path.home() / '.termhub', config='config.json'):
    if not path.exists() or not (path / config).exists():
        return False
    return True


def read_config_file(path=pathlib.Path.home() / '.termhub', config='config.json'):
    if not path.exists():
        path.mkdir()
    filepath = path / config

    if not filepath.exists():
        create_default_config_file()
        # TODO: Fix temporary solution
        filepath.touch()

    with filepath.open("r", encoding="utf-8") as file:
        print(file.read())


if __name__ == '__main__':
    start()
