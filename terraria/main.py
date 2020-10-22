# Port of: Terraria.Main
from os import system
from random import Random

from terraria.game import Game
from terraria.io.world_file_data import WorldFileData
from terraria.lang import Lang
from terraria.localization.language import Language
from terraria.npc import NPC


class Main(Game):
    # Static vars go here
    instance = None
    var_ded_serv = False  # this is the port of "public static bool dedServ = false;"
    expert_mode = False
    active_world_file_data = WorldFileData()
    world_path_name = active_world_file_data.path
    versionNumber = 'v1.3.0.7.5'
    versionNumber2 = 'v1.3.0.7.5'
    world_list = []

    def __init__(self):
        super().__init__()
        self.offlimit_border_tiles = 40
        self.max_item_types = 3602
        self.max_projectile_types = 651
        self.max_npc_types = 540
        self.max_tile_sets = 419
        self.max_wall_types = 225
        self.max_buff_types = 191
        self.max_glow_masks = 214
        self.auto_shutdown = False
        self.show_splash = True
        self.npc_name = [None] * 540    # this is a list of 540 strings that will contain npc names

        # This line was the content of the actual constructor in the original Main
        Main.instance = self
        return

    def ded_serv(self):
        rand = Random()

        if self.auto_shutdown:
            # To-DO: port the functionality
            pass
        else:
            # system("Python Terraria Mobile Server " + self.versionNumber2)
            pass
        Main.var_ded_serv = True
        self.show_splash = False
        self.initialize()
        Lang.set_lang(english=True)

        for i in range(540):
            npc = NPC()
            npc.set_defaults(i)
            self.npc_name[i] = npc.name

        while Main.world_path_name is None or Main.world_path_name == '':
            flag = True
            while flag:
                Main.load_worlds()
                print(Language.get_text_value('CLI.MobileServer', Main.versionNumber2))

                for j in range(len(Main.world_list)):
                    print(f'{j+1}       {Main.world_list[j].name}')


    def initialize(self):
        pass
