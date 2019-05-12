import pathlib

configFile = "config.json"
path = pathlib.Path(str(pathlib.Path.home()) + "/.termhub")
if not path.exists():
    path.mkdir()
filepath = path / configFile
with filepath.open("r", encoding="utf-8") as f:
    print(f.read())
print(path)