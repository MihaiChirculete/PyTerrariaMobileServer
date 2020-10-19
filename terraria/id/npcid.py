from pytms.utils.color import Color
from terraria.id.set_factory import SetFactory


class NPCID:
    class Sets:
        factory = SetFactory(540)
        needs_expert_scaling = factory.create_bool_set(25, 30, 33, 112, 261, 265, 371, 516, 519, 522, 397, 396, 398)
        projectile_NPC = factory.create_bool_set(25, 30, 33, 112, 261, 265, 371, 516, 519, 522)
        saves_and_loads = factory.create_bool_set(422, 507, 517, 493)
        trail_cache_length = factory.create_int_set(10, 402, 36, 519, 20, 522, 20)
        mp_allowed_enemies = factory.create_bool_set(4, 13, 50, 126, 125, 134, 127, 128, 131, 129, 130, 222, 245, 266,
                                                     370)
        town_critter = factory.create_bool_set(46, 148, 149, 230, 299, 300, 303, 337, 361, 362, 364, 366, 367, 443, 445,
                                               447, 538, 539)
        face_emote = factory.create_int_set(0, 17, 101, 18, 102, 19, 103, 20, 104, 22, 105, 37, 106, 38, 107, 54, 108,
                                            107, 109, 108, 110, 124, 111, 142, 112, 160, 113, 178, 114, 207, 115, 208,
                                            116, 209, 117, 227, 118, 228, 119, 229, 120, 353, 121, 368, 122, 369, 123,
                                            453, 124, 441, 125)
        extra_frames_count = factory.create_int_set(0, 17, 9, 18, 9, 19, 9, 20, 7, 22, 10, 37, 5, 38, 9, 54, 7, 107, 9,
                                                    108, 7, 124, 9, 142, 9, 160, 7, 178, 9, 207, 9, 208, 9, 209, 10,
                                                    227, 9, 228, 10, 229, 10, 353, 9, 368, 10, 369, 9, 453, 9, 441, 9)
        attack_frame_count = factory.create_int_set(0, 17, 4, 18, 4, 19, 4, 20, 2, 22, 5, 37, 0, 38, 4, 54, 2, 107, 4,
                                                    108, 2, 124, 4, 142, 4, 160, 2, 178, 4, 207, 4, 208, 4, 209, 5, 227,
                                                    4, 228, 5, 229, 5, 353, 4, 368, 5, 369, 4, 453, 4, 441, 4)
        danger_detect_range = factory.create_int_set(-1, 38, 300, 17, 320, 107, 300, 19, 900, 22, 700, 124, 800, 228,
                                                     800, 178, 900, 18, 300, 229, 1000, 209, 1000, 54, 700, 108, 700,
                                                     160, 700, 20, 1200, 369, 300, 453, 300, 368, 900, 207, 60, 227,
                                                     800, 208, 400, 142, 500, 441, 50, 353, 60)
        attack_time = factory.create_int_set(-1, 38, 34, 17, 34, 107, 60, 19, 40, 22, 30, 124, 34, 228, 40, 178, 24, 18,
                                             34, 229, 60, 209, 60, 54, 60, 108, 30, 160, 60, 20, 600, 369, 34, 453, 34,
                                             368, 60, 207, 15, 227, 60, 208, 34, 142, 34, 441, 15, 353, 12)
        attack_type = factory.create_int_set(-1, 38, 0, 17, 0, 107, 0, 19, 1, 22, 1, 124, 0, 228, 1, 178, 1, 18, 0, 229,
                                             1, 209, 1, 54, 2, 108, 2, 160, 2, 20, 2, 369, 0, 453, 0, 368, 1, 207, 3,
                                             227, 1, 208, 0, 142, 0, 441, 3, 353, 3)
        pretty_safe = factory.create_int_set(-1, 19, 300, 22, 200, 124, 200, 228, 300, 178, 300, 229, 300, 209, 300, 54,
                                             100, 108, 100, 160, 100, 20, 200, 368, 200, 227, 200)
        magic_aura_color = factory.create_custom_set(Color.white, 54, Color(100, 4, 227, 127), 108,
                                                     Color(255, 80, 60, 127), 160, Color(40, 80, 255, 127), 20,
                                                     Color(40, 255, 80, 127))

    big_hornet_stingy = -65
    little_hornet_stingy = -64
    big_hornet_spikey = -63
    little_hornet_spikey = -62
    big_hornet_leafy = -61
    little_hornet_leafy = -60
    big_hornet_honey = -59
    little_hornet_honey = -58
    big_hornet_fatty = -57
    # TO-DO: Add the rest of the id's

    net_id_map = [81,
                  81,
                  1,
                  1,
                  1,
                  1,
                  1,
                  1,
                  1,
                  1,
                  6,
                  6,
                  31,
                  31,
                  77,
                  42,
                  42,
                  176,
                  176,
                  176,
                  176,
                  173,
                  173,
                  183,
                  183,
                  3,
                  3,
                  132,
                  132,
                  186,
                  186,
                  187,
                  187,
                  188,
                  188,
                  189,
                  189,
                  190,
                  191,
                  192,
                  193,
                  194,
                  2,
                  200,
                  200,
                  21,
                  21,
                  201,
                  201,
                  202,
                  202,
                  203,
                  203,
                  223,
                  223,
                  231,
                  231,
                  232,
                  232,
                  233,
                  233,
                  234,
                  234,
                  235,
                  235]

    @staticmethod
    def from_net_id(id_num):
        id_num = int(id_num)

        if id_num < 0:
            return NPCID.net_id_map[-id_num - 1]

        return id_num
