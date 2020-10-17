class Entity:
    def __init__(self):
        self.who_am_i: int
        self.active: bool
        # self.position :Vector2
        # self.velocity :Vector2
        # self.old_position :Vector2
        # self.old_velocity :Vector2
        self.old_direction: int
        self.direction = 1
        self.width: int
        self.height: int
        self.wet: bool
        self.honey_wet: bool
        self.wet_count: int # was byte in original
        self.lava_wet: bool

# TO-DO: PORT THE METHODS
