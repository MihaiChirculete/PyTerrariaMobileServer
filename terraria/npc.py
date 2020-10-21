from pytms.utils.color import Color
from pytms.utils.rectangle import Rectangle
from pytms.utils.vector2 import Vector2
from terraria.entity import Entity
from terraria.id.npcid import NPCID
from terraria.lang import Lang
from terraria.localization.language import Language


class NPC(Entity):
    # static fields go here
    moon_lord_countdown = 0
    immune_time = 20
    max_AI = 4
    gold_critter_chance = 150
    kill_count = [None] * 540  # public static int[] killCount = new int[540];
    wave_kills = float(0)
    wave_count = 0
    tax_collector = False
    spawn_space_x = 3
    spawn_space_y = 3
    gravity = 0.3
    max_attack = 20
    attack_NPC = [None] * max_attack
    fire_fly_friendly = 0
    fire_fly_chance = 0
    fire_fly_multiple = 0
    butterfly_chance = 0
    golem_boss = -1
    plant_boss = -1
    crimson_boss = -1
    s_width = 1920
    s_height = 1080
    spawn_range_x = int(float(s_width / 16) * 0.7)
    spawn_range_y = int(float(s_height / 16) * 0.7)
    safe_range_x = int(float(s_width / 16) * 0.52)
    safe_range_y = int(float(s_height / 16) * 0.52)
    active_range_x = int(float(s_width) * 2.1)
    active_range_y = int(float(s_height) * 2.1)
    town_range_x = s_width
    town_range_y = s_height
    no_spawn_cycle = False
    active_time = 750
    default_spawn_rate = 600
    default_max_spawns = 5
    saved_tax_collector = False
    saved_goblin = False
    saved_wizard = False
    saved_mech = False
    saved_angler = False
    saved_stylist = False
    downed_boss1 = False
    downed_boss2 = False
    downed_boss3 = False
    downed_queen_bee = False
    downed_slime_king = False
    downed_goblins = False
    downed_frost = False
    downed_pirates = False
    downed_clown = False
    downed_plant_boss = False
    downed_golem_boss = False
    downed_martians = False
    downed_fishron = False
    downed_halloween_tree = False
    downed_halloween_king = False
    downed_christmas_ice_queen = False
    downed_christmas_santank = False
    downed_ancient_cultist = False
    downed_moon_lord = False
    downed_tower_solar = False
    downed_tower_vortex = False
    downed_tower_nebula = False
    downed_tower_stardust = False
    shield_strength_tower_solar = 0
    shield_strength_tower_vortex = 0
    shield_strength_tower_nebula = 0
    shield_strength_tower_stardust = 0
    lunar_shield_power_normal = 100
    lunar_shield_power_expert = 150
    tower_active_solar = False
    tower_active_vortex = False
    tower_active_nebula = False
    tower_active_stardust = False
    lunar_apocalypse_is_up = False
    downed_mech_boss_any = False
    downed_mech_boss1 = False
    downed_mech_boss2 = False
    downed_mech_boss3 = False
    spawn_rate = default_spawn_rate
    max_spawns = default_max_spawns
    travel_NPC = False
    cavern_monster_type = [[None] * 2, [None] * 3]  # public static int[,] cavernMonsterType = new int[2, 3];
    ignore_player_interactions = 0

    def __init__(self):
        self.active = True
        self.wet = False
        self.wet_count: int = None
        self.lava_wet: bool = None
        self.max_moon_lord_countdown = 3600
        self.max_buffs = 5
        self.breath_max = 200
        self.name = ''
        # public static readonly int[,,,] MoonLordAttacksArray = InitializeMoonLordAttacks();
        # public static readonly int[,] MoonLordAttacksArray2 = InitializeMoonLordAttacks2();
        self.teleport_style: int = None
        self.teleport_time: float = None
        self.net_spam: int = None
        self.dripping: bool = None
        self.dripping_slime: bool = None
        self.catch_item: int = None  # was short in original file
        self.release_owner = 255  # was short in original file
        self.rarity: int = None
        self.player_interaction = [None] * 17  # public bool[] playerInteraction = new bool[17];
        self.last_interaction = 16
        self.taken_damage_multiplier = float(1)
        self.gfxOffY: float = None
        self.step_speed: float = None
        self.teleporting: bool = None
        self.stair_fall: bool = None
        self.net_stream: bytes = None  # private byte netStream;
        self.stream_player = [None] * 16  # private byte[] streamPlayer = new byte[16];
        self.npc_name_lookup: bytes = None  # private byte npcNameLookup;
        self.old_pos = [Vector2()] * 10
        self.old_rot = [None] * 10  # public float[] oldRot = new float[10];
        self.set_frame_size: bool = None
        self.net_skip: int = None
        self.net_always: bool = None
        self.real_life = -1
        self.npc_slots = float(1)
        self.dont_count_me: bool = None
        self.buff_type = [None] * 5
        self.buff_time = [None] * 5
        self.buff_immune = [None] * 191
        self.midas: bool = None
        self.ichor: bool = None
        self.on_fire: bool = None
        self.on_fire2: bool = None
        self.on_frost_burn: bool = None
        self.poisoned: bool = None
        self.venom: bool = None
        self.shadow_flame: bool = None
        self.soul_drain: bool = None
        self.life_regen: int = None
        self.life_regen_count: int = None
        self.confused: bool = None
        self.love_struck: bool = None
        self.stinky: bool = None
        self.dryad_ward: bool = None
        self.immortal: bool = None
        self.chaseable = True
        self.can_ghost_heal = True
        self.javelined: bool = None
        self.celled: bool = None
        self.dryad_bane: bool = None
        self.daybreak: bool = None
        self.sound_delay: int = None
        self.immune = [None] * 17
        self.direction_y = 1
        self.type: int = None
        self.ai = [None] * NPC.max_AI
        self.local_AI = [None] * NPC.max_AI
        self.ai_action: int = None
        self.ai_style: int = None
        self.just_hit: bool = None
        self.time_left: int = None
        self.target = -1
        self.damage: int = None
        self.defense: int = None
        self.def_damage: int = None
        self.def_defense: int = None
        self.cold_damage: bool = None
        self.trap_immune: bool = None
        self.sound_hit: int = None
        self.sound_killed: int = None
        self.life: int = None
        self.life_max: int = None
        self.target_rect = Rectangle()  # public Rectangle targetRect;
        self.frame_counter: float = None  # was double in original
        self.frame = Rectangle()  # public Rectangle frame;
        self._given_name = ''
        self.has_given_name = lambda x: len(self._given_name) != 0
        self.color = Color()  # public Color color
        self.alpha: int = None
        self.hide: bool = None
        self.scale = float(1)
        self.knock_back_resist = float(1)
        self.old_direction: int = None  # public new int oldDirection; // not sure why this is defined twice in the original
        self.old_direction_y: int = None
        self.old_target: int = None
        self.rotation: float = None
        self.no_gravity: bool = None
        self.no_tile_collide: bool = None
        self.net_update: bool = None
        self.net_update2: bool = None
        self.collide_x: bool = None
        self.collide_y: bool = None
        self.boss: bool = None
        self.sprite_direction = -1
        self.behind_tiles: bool = None
        self.lava_immune: bool = None
        self.value: float = None
        self.extra_value: float = None
        self.dont_take_damage: bool = None
        self.net_ID: int = None
        self.town_NPC: bool = None
        self.homeless: bool = None
        self.home_tile_x = -1
        self.home_tile_y = -1
        self.old_homeless: bool = None
        self.old_home_tile_x = -1
        self.old_home_tile_y = -1
        self.friendly: bool = None
        self.close_door: bool = None
        self.door_x: int = None
        self.door_y: int = None
        self.friendly_regen: int = None
        self.breath: int = None
        self.breath_counter: int = None
        self.reflecting_projectiles: bool = None
        self.last_portal_color_index: int = None
        self.type_name: str = Lang.get_NPC_name_value(self.net_ID)

    @staticmethod
    def downed_towers():
        if NPC.downed_tower_solar and NPC.downed_tower_vortex and NPC.downed_tower_nebula:
            return NPC.downed_tower_stardust
        return False

    @staticmethod
    def shield_strength_tower_max():
        from terraria.main import Main
        if not Main.expert_mode:
            return NPC.lunar_shield_power_normal
        return NPC.lunar_shield_power_expert

    @staticmethod
    def towers_defeated():
        if NPC.tower_active_solar and NPC.tower_active_vortex and NPC.tower_active_nebula:
            return NPC.tower_active_stardust
        return False

    # public string TypeName => Lang.GetNPCNameValue(netID);

    def full_name(self):
        if not self.has_given_name:
            return self.type_name
        return Language.get_text_value('Game.NPCTitle', self._given_name, self.type_name)

    def given_or_type_name(self):
        if not self.has_given_name:
            return self.type_name
        return self._given_name

    def get_given_name(self):
        return self._given_name

    def set_given_name(self, name=''):
        self._given_name = name

    def get_opacity(self):
        return float(1) - float(self.alpha) / float(255)

    def set_opacity(self, value):
        # alpha = (int)MathHelper.Clamp((1f - value) * 255f, 0f, 255f);
        self.alpha = int(max(float(0), min((float(1) - value) * float(255), float(255))))

    def can_talk(self):
        if (self.town_NPC or self.type == 453) or self.ai_style == 7:
            # original: return velocity.Y == 0f;
            return True
        return False

    def has_valid_target(self):
        from terraria.main import Main

        if 0 <= self.target < 16 and Main.player[self.target].active:
            return not Main.player[self.target].dead
        return False

    @staticmethod
    def initialize_moon_lord_attacks():
        # TO-DO: Port the code
        return None

    @staticmethod
    def get_first_npc_name_or_null(npc_type: int):
        from terraria.main import Main

        for i in range(200):
            if Main.npc[i].active and Main.npc[i].type == npc_type:
                return Main.npc[i].given_or_type_name

        return None

    def set_defaults(self, type: int, scale_override: float = -1):
        self.taken_damage_multiplier = float(1)
        self.extra_value = float(0)
        for i in range(len(self.player_interaction)):
            self.player_interaction[i] = False
        self.rarity = 0
        self.dont_count_me = False
        self.release_owner = 255
        self.catch_item = 0
        self.npc_name_lookup = 0
        self.net_stream = 32
        flag = False
        self.net_ID = 0
        self.net_spam = 0
        num = 10

        if type >= 0:
            num = NPCID.Sets.trail_cache_length[type]
            pass

        if type != len(self.old_pos):
            # Array.Resize(ref oldPos, num);
            # Array.Resize(ref oldRot, num);
            pass

        for j in range(len(self.old_pos)):
            self.old_rot[j] = float(0)
            self.old_pos[j].x = float(0)
            self.old_pos[j].y = float(0)

        for k in range(5):
            self.buff_time[k] = 0
            self.buff_time[k] = 0

        for l in range(191):
            self.buff_immune[l] = False

        self.set_frame_size = False
        self.buff_immune[31] = True
        self.net_skip = -2
        self.real_life = -1
        self.life_regen = 0
        self.life_regen_count = 0
        self.poisoned = False
        self.soul_drain = False
        self.venom = False
        self.shadow_flame = False
        self.on_fire = False
        self.midas = False
        self.ichor = False
        self.on_frost_burn = False
        self.confused = False
        self.love_struck = False
        self.stinky = False
        self.dryad_ward = False
        self.on_fire2 = False
        self.just_hit = False
        self.dont_take_damage = False
        self.npc_slots = float(1)
        self.lava_immune = False
        self.lava_wet = False
        self.wet_count = 0
        self.wet = False
        self.town_NPC = False
        self.homeless = False
        self.home_tile_x = -1
        self.home_tile_y = -1
        self.friendly = False
        self.behind_tiles = False
        self.boss = False
        self.no_tile_collide = False
        self.rotation = float(0)
        self.active = True
        self.alpha = 0
        self.color = Color()
        self.collide_x = False
        self.collide_y = False
        self.direction = 0
        self.old_direction = self.direction
        self.frame_counter = float(0.0)
        self.net_update = True
        self.net_update2 = False
        self.knock_back_resist = float(1)
        self._given_name = ''
        self.name = ''
        self.no_gravity = False
        self.scale = float(1)
        self.sound_hit = 0
        self.sound_killed = 0
        self.sprite_direction = -1
        self.target = 16
        self.old_target = self.target
        self.target_rect = Rectangle()
        self.time_left = self.active_time
        self.type = type
        self.value = float(0)
        self.cold_damage = False
        self.trap_immune = False
        self.hide = False
        self.immortal = False
        self.chaseable = True
        self.breath = 200
        self.breath_counter = 0
        self.reflecting_projectiles = False
        self.can_ghost_heal = True
        self.javelined = False
        self.daybreak = False
        self.celled = False
        self.dryad_bane = False

        for m in range(self.max_AI):
            self.ai[m] = float(0)

        for n in range(self.max_AI):
            self.local_AI[n] = float(0)

        if type == 1:
            self.name = 'Blue Slime'
            self.width = 24
            self.height = 18
            self.ai_style = 1
            self.damage = 7
            self.defense = 2
            self.life_max = 25
            self.sound_hit = 1
            self.sound_killed = 1
            self.alpha = 175
            self.color = Color(0, 80, 255, 100)
            self.value = float(25)
            self.buff_immune[20] = True
            self.buff_immune[31] = False

        elif type == 2:
            self.name = 'Demon Eye'
            self.width = 30
            self.height = 32
            self.ai_style = 2
            self.damage = 18
            self.defense = 2
            self.life_max = 60
            self.sound_hit = 1
            self.knock_back_resist = float(0.8)
            self.sound_killed = 1
            self.value = float(75)
            self.buff_immune[31] = False



