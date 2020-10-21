class Entity:
    def __init__(self):
        self.who_am_i: int = None
        self.active: bool = None
        # self.position :Vector2
        # self.velocity :Vector2
        # self.old_position :Vector2
        # self.old_velocity :Vector2
        self.old_direction: int = None
        self.direction = 1
        self.width: int = None
        self.height: int = None
        self.wet: bool = None
        self.honey_wet: bool = None
        self.wet_count: int = None # was byte in original
        self.lava_wet: bool = None

# TO-DO: PORT THE METHODS
