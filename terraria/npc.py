from terraria.entity import Entity
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
        self.max_moon_lord_countdown = 3600
        self.max_buffs = 5
        self.breath_max = 200
        self.name = ''
        # public static readonly int[,,,] MoonLordAttacksArray = InitializeMoonLordAttacks();
        # public static readonly int[,] MoonLordAttacksArray2 = InitializeMoonLordAttacks2();
        self.teleport_style: int
        self.teleport_time: float
        self.net_spam: int
        self.dripping: bool
        self.dripping_slime: bool
        self.catch_item: int  # was short in original file
        self.release_owner = 255  # was short in original file
        self.rarity: int
        self.player_interaction = [None] * 17  # public bool[] playerInteraction = new bool[17];
        self.last_interaction = 16
        self.taken_damage_multiplier = float(1)
        self.gfxOffY: float
        self.step_speed: float
        self.teleporting: bool
        self.stair_fall: bool
        self.net_stream: bytes  # private byte netStream;
        self.stream_player = [None] * 16  # private byte[] streamPlayer = new byte[16];
        self.npc_name_lookup: bytes  # private byte npcNameLookup;
        self.old_pos = [None] * 10  # public Vector2[] oldPos = new Vector2[10];
        self.old_rot = [None] * 10  # public float[] oldRot = new float[10];
        self.set_frame_size: bool
        self.net_skip: int
        self.net_always: bool
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
        self.just_hit: bool
        self.time_left: int
        self.target = -1
        self.damage: int
        self.defense: int
        self.def_damage: int
        self.def_defense: int
        self.cold_damage: bool
        self.trap_immune: bool
        self.sound_hit: int
        self.sound_killed: int
        self.life: int
        self.life_max: int
        # public Rectangle targetRect;
        self.frame_counter: float  # was double in original
        # public Rectangle frame;
        self._given_name = ''
        self.has_given_name = lambda x: len(self._given_name) != 0
        # public Color color
        self.alpha: int = None
        self.hide: bool
        self.scale = float(1)
        self.knock_back_resist = float(1)
        self.old_direction: int  # public new int oldDirection; // not sure why this is defined twice in the original
        self.old_direction_y: int
        self.old_target: int
        self.rotation: float
        self.no_gravity: bool
        self.no_tile_collide: bool
        self.net_update: bool
        self.net_update2: bool
        self.collide_x: bool
        self.collide_y: bool
        self.boss: bool
        self.sprite_direction = -1
        self.behind_tiles: bool = None
        self.lava_immune: bool = None
        self.value: float = None
        self.extra_value: float = None
        self.dont_take_damage: bool = None
        self.net_ID: int
        self.town_NPC: bool = None
        self.homeless: bool = None
        self.home_tile_x = -1
        self.home_tile_y = -1
        self.old_homeless: bool
        self.old_home_tile_x = -1
        self.old_home_tile_y = -1
        self.friendly: bool
        self.close_door: bool
        self.door_x: int
        self.door_y: int
        self.friendly_regen: int
        self.breath: int
        self.breath_counter: int
        self.reflecting_projectiles: bool
        self.last_portal_color_index: int
        self.type_name: str = Lang.get_NPC_name_value(self.net_ID)

    @staticmethod
    def downed_towers():
        if NPC.downed_tower_solar and NPC.downed_tower_vortex and NPC.downed_tower_nebula:
            return NPC.downed_tower_stardust
        return False

    @staticmethod
    def shield_strength_tower_max():
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
