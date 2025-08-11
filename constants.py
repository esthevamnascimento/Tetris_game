# tetris/constants.py
"""
Módulo de constantes do jogo Tetris.

Aqui definimos todas as configurações fixas do jogo como:
- Tamanho da tela
- Cores
- Formatos das peças
- Velocidades
"""

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Cores (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

# Mapeamento de cores para as peças
COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, MAGENTA, RED]

# Formatos das peças (tetrominós)
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]  # Z
]

# Configurações do jogo
FPS = 60
INITIAL_SPEED = 0.5  # segundos por movimento para baixo
SPEED_INCREASE = 0.95  # fator de aumento de velocidade por nível