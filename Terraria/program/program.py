# Port of: Terraria.Program
import datetime


def display_exception(e):
    print(f'Server crash: {datetime.time.strftime("%H:%M")}')
    print(e)


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
            main.DedServ()
        except Exception as e:
            display_exception(e)
