import pathlib


class Config:
    def __init__(self): pass

    def load(self, json): pass


def create_default_config_file():
    pass


def load_config():
    pass


def write_config(config, file):
    pass


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
    read_config_file()
