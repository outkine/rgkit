settings = {
    # game settings
    'spawn_every': 10,
    'spawn_per_player': 5,
    'board_size': 19,
    'robot_hp': 50,
    'attack_range': (8, 10),
    'collision_damage': 5,
    'suicide_damage': 15,
    'max_turns': 100,

    # rendering
    # commented out lines are the settings used for the old animated mode 
    'FPS': 60,  # frames per second
    'turn_interval': 300,  # milliseconds per turn
    'colors': [(0.49, 0.14, 0.14), (0.14, 0.49, 0.14)],
    # 'colors': [(0.9, 0, 0.2), (0, 0.9, 0.2)],
    'obstacle_color': (.2, .2, .2),
    'normal_color': (.9, .9, .9),
    'highlight_color': (0.6, 0.6, 0.6),
    'target_color': (0.6, 0.6, 1),
    'clear_highlight_between_turns': False,
    # 'clear_highlight_between_turns': True,
    'clear_highlight_target_between_turns': True,
    'highlight_cursor_blink': False,
    # 'highlight_cursor_blink': True,
    'highlight_cursor_blink_interval': 0.5,
    'bot_shape': 'square',
    # 'bot_shape': 'circle',
    'bot_animate': False,
    # 'bot_animate': True,
    'draw_movement_arrow': True,
    # 'draw_movement_arrow': False,

    # rating systems
    'rating_range': 150,
    'default_rating': 1200,

    # user-scripting
    'max_usercode_time': 1500,
    'exposed_properties': ('location', 'hp', 'player_id'),
    'player_only_properties': ('robot_id',),
    'user_obj_types': ('Robot',),
    'valid_commands': ('move', 'attack', 'guard', 'suicide'),
    'user_modules': ('numpy', 'euclid', 'random'),
}

# just change stuff above this line

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
settings = AttrDict(settings)