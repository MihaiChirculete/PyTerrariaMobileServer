# Port of: Terraria.Main
from os import system
from random import Random

from terraria.game import Game


class Main(Game):
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
        self.versionNumber = 'v1.3.0.7.5'
        self.versionNumber2 = 'v1.3.0.7.5'
        self.var_ded_serv = False   # this is the port of "public static bool dedServ = false;"
        self.show_splash = True
        return

    def ded_serv(self):
        rand = Random()

        if self.auto_shutdown:
            pass
        else:
            system("Python Terraria Mobile Server " + self.versionNumber2)

        self.var_ded_serv = True
        self.show_splash = False
        self.initialize()



    def initialize(self):
        pass
