# Port of: Terraria.Program
from datetime import datetime
import traceback

from terraria.main import Main


def display_exception(e: Exception):
    traceback.print_exc()
    print(f'{datetime.now().strftime("%H:%M:%S")} Server crash: {e}')


class Program:
    def __init__(self):
        self.is_server = True
        self.launch_params = None  # This will be a dictionary of the form {arg: 'value'}

    def launch_game(self, args: list):
        self.launch_params = {key: value for key, value in args}
        main = Main()

        try:
            #SocialAPI.Initialize()
            #LaunchInitializer.LoadParameters(main)
            main.ded_serv()
        except Exception as e:
            display_exception(e)
