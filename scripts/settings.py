WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
    "player": -26,
    "object": -40,
    "grass": -10,
    "invisible": 0
}

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT ="graphics/my_tilesets/font/NormalFont.ttf"
UI_FONT_SIZE = 18

WATER_COLOR = '#71ddee'
UI_BG_COLOR = "#222222"
UI_BORDER_COLOR = "#111111"
TEXT_COLOR = "#EEEEEE"

HEALTH_COLOR = "red"
ENERGY_COLOR = "blue"
UI_BORDER_COLOR_ACTIVE = "gold"

TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = "#EEEEEE"
BAR_COLOR_SELECTED ='#111111'
UPGRADE_BG_COLOR_SELECTED = "#EEEEEE"

weapon_data = {
    'sword':{'cooldown': 200, 'damage': 15, 'graphic':'graphics/my_tilesets/weapons/sword/up.png'},
    'axe':{'cooldown': 400, 'damage': 20, 'graphic':'graphics/my_tilesets/weapons/axe/up.png'},
    'katana':{'cooldown': 100, 'damage': 10, 'graphic':'graphics/my_tilesets/weapons/katana/up.png'},
    'hammer':{'cooldown': 500, 'damage': 25, 'graphic':'graphics/my_tilesets/weapons/hammer/up.png'},
}

magic_data = {
    "flame":{'strength': 17.5, "cost": 20, "graphic": "graphics/my_tilesets/particles/flame/0.png"},
    "heal":{'strength': 20, "cost": 10, "graphic": "graphics/my_tilesets/particles/heal/1.png"}
}


monster_data = {
    "bamboo": {"health": 70, "exp": 100, "damage": 6, 'attack_type': "leaf_attack", "attack_sound":"graphics/my_tilesets/audio/attack/Hit1.wav", "speed": 2, "resistance": 3, "attack_radius": 50, "notice_radius":500},
    "cyclope": {"health": 100, "exp": 110, "damage": 5, 'attack_type': "thunder_attack", "attack_sound":"graphics/my_tilesets/audio/attack/Hit4.wav", "speed": 3, "resistance": 3, "attack_radius": 75, "notice_radius":550}
}