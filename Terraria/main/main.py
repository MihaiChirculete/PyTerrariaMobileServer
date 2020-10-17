# Port of: Terraria.Main

from Terraria.server.game import Game


class Main(Game):
    def __init__(self):
        self.offlimit_border_tiles = 40
        self.max_item_types = 3602
        self.max_projectile_types = 651
        return
