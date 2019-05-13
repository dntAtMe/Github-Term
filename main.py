import pathlib

# TODO: Create config if empty folder exists
configFile = "config.json"
path = pathlib.Path.home() / '.termhub'
print(path)
filepath = path / configFile
if not path.exists():
    path.mkdir()
    filepath.touch()
with filepath.open("r", encoding="utf-8") as f:
    f.readable()
