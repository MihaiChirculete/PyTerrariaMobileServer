# Terraria.Lang
from terraria.localization.localized_text import LocalizedText


class Lang:
    lang = 0
    misc = [None] * 105
    menu = [None] * 253
    gen = [None] * 82
    inter = [None] * 118
    tip = [None] * 60
    mp = [None] * 23
    dt = [None] * 4
    chest_type = [None] * 52
    dresser_type = [None] * 28
    mobile = [None] * 120
    the = ''    # dunno wtf this one is
    _item_name_cache = [None] * 3602
    _negative_item_name_cache = [None] * 24
    _projectile_name_cache = [None] * 651
    _NPC_name_cache = [None] * 540
    _negative_NPC_name_cache = [None] * 65
    _buff_name_cache = [None] * 191
    _buff_description_cache = [None] * 191
    prefix = [None] * 84
    _map_legend_cache = [None]
    _item_tooltip_cache = [None] * 3602
    _negative_item_tooltip_cache = [None] * 24


    def __init__(self):
        pass

    @staticmethod
    def set_lang(english=False):
        pass

    @staticmethod
    def get_NPC_name_value(net_id=0):
        net_id = 0 if net_id is None else net_id    # make sure we didnt get a NoneType object
        return Lang.get_NPC_name(net_id).get_value()

    @staticmethod
    def get_NPC_name(net_id) -> LocalizedText:
        if 0 < net_id < 540:
            return Lang._NPC_name_cache[net_id]
        if net_id < 0 and -net_id - 1 < len(Lang._negative_NPC_name_cache):
            return Lang._negative_NPC_name_cache[-net_id - 1]

        return LocalizedText.empty()
