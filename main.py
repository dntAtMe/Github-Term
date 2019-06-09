import pathlib
import json
import requests

class Query:
    def __init__(self, content = ''):
        self.content = content

    @staticmethod
    def build_query():
        return Query()

    def build_viewer(self, *args):

        args = ' '.join(args)
        self.content += 'viewer {{ {} }}'.format(args)
        return self

    def wrap(self):
        self.content = '{{ {} }}'.format(self.content)
        return self.content

    def __str__(self):
        json.dumps(self.content)


def run_query(query):
    """Runs given GraphQL query in GitHub API"""
    headers = {"Authorization": "Bearer {}".format(get_token())}
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


class Config:
    """Stores User API Key and app configuration"""

    def __init__(self): pass

    def load(self, json): pass


def create_default_config_file():
    path = pathlib.Path.home() / '.termhub'
    config='config.json'

    if not path.exists():
        path.mkdir()

    filepath = path / config

    # TODO: Fix temporary solution
    filepath.touch()

    data = {}
    data['token'] = input("Personal access token: ")

    with filepath.open("w", encoding="utf-8") as file:
        json.dump(data, file)


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
            answer = input("Create default config file? (Y/N)").upper()
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


def get_token(path=pathlib.Path.home() / '.termhub', config='config.json'):
    filepath = path / config
    data = {}

    if not filepath.exists():
        create_default_config_file()
        # TODO: Fix temporary solution

    with filepath.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return data['token']


def read_config_file(path=pathlib.Path.home() / '.termhub', config='config.json'):
    filepath = path / config

    if not filepath.exists():
        create_default_config_file()
        # TODO: Fix temporary solution

    with filepath.open("r", encoding="utf-8") as file:
        print(file.read())


if __name__ == '__main__':
    start()
    query = """
    {
      viewer {
        repositories(first:100) {
          nodes {
            name
                    issues(first:100) {
                nodes {
                title
                body
              }  
            }       
          }
        }
      } 
    }
    """
    query = Query.build_query().build_viewer("id", "login").wrap()
    print(query)
    result = run_query(query)  # Execute the query
    print(result)
