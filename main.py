from requests import get
from subprocess import run, PIPE
from json import loads

from lobby import Crasher
import configparser

from os import system

class Interface:
    def __init__(self) -> None:
        self.league_path = None
        self.read_config()

        self.crasher = Crasher(self.league_path)
        self.display()
    
    def read_config(self, file_path="settings.ini"):
        config = configparser.ConfigParser()
        try:
            config.read(file_path)
            self.league_path = config.get("League", "path")
        except configparser.Error as e:
            print(f"Error reading config file: {e}")
    
    def prompt(self):
        system("cls")
        print(""" _       _     _                                _               
| |     | |   | |                              | |              
| | ___ | |__ | |__  _   _    ___ _ __ __ _ ___| |__   ___ _ __ 
| |/ _ \| '_ \| '_ \| | | |  / __| '__/ _` / __| '_ \ / _ | '__|
| | (_) | |_) | |_) | |_| | | (__| | | (_| \__ | | | |  __| |   
|_|\___/|_.__/|_.__/ \__, |  \___|_|  \__,_|___|_| |_|\___|_|   
                      __/ |                                     
                     |___/                                      
        """)
        
        print(f"Summoner: {self.crasher.summoner['displayName']}")
        print(f"Target Lobby: {self.crasher.target_lobby_id}\n")

        print("1. Set target lobby")
        print("2. Escape current lobby")
        print("3. Leave\n")

    def display(self):
        while True:
            self.prompt()
            try:
                selected_option = int(input("> "))

                match(selected_option):
                    case 1:
                        player_name = input("\nSummoner name of custom lobby host: ")
                        self.crasher.set_lobby(player_name)
                        system("pause")
                    case 2:
                        self.crasher.crash()
                        system("pause")
                    case 3:
                        break
            except ValueError:
                print("Invalid option.")


if __name__ == "__main__":
    Interface()
