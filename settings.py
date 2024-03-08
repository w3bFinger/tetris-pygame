import pygame

# GAME SIZE
colums = 10
rows = 20
cell_size = 40
game_width, game_height = colums * cell_size, rows * cell_size

sidebar_width = 200
preview_height_fraction = 0.7
score_height_fraction = 1 - preview_height_fraction

# WINDOW
padding = 20
windows_width = game_width + sidebar_width + padding * 3
window_height = game_height + padding * 2

# GAME BEHAVIOUR
update_start_speed = 800
move_wait_time = 200
rotate_wait_time = 200
block_offset = pygame.Vector2(colums // 2, -1)

# COLORS
yellow = "#f1e60d"
red = "#e51b20"
blue = "#204b9b"
green = "#65b32e"
purple = "#7b217f"
cyan = "#6cc6d9"
orange = "#f07e13"
gray = "#1C1C1C"
line_color = "#FFFFFF"

# shapes
tetrominos = {
    'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': purple},
    'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': yellow},
    'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': blue},
    'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': orange},
    'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': cyan},
    'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': green},
    'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': red},
}