# tetris/view.py
"""
Módulo View do jogo Tetris.

Responsável por toda a renderização gráfica do jogo:
- Desenho do grid
- Desenho das peças
- Exibição de informações (pontuação, próximo peça)
- Tela de game over
"""
import pygame
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, GRID_WIDTH, 
                      GRID_HEIGHT, BLACK, WHITE, GRAY)

class TetrisView:
    def __init__(self):
        """Inicializa a visualização do jogo."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris Educativo')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        
    def draw(self, model):
        """Desenha todo o estado do jogo."""
        self.screen.fill(BLACK)
        
        # Desenha o grid principal
        self._draw_grid(model.grid)
        
        # Desenha a peça atual
        self._draw_piece(model.current_piece)
        
        # Desenha a próxima peça
        self._draw_next_piece(model.next_piece)
        
        # Desenha informações do jogo
        self._draw_game_info(model.score, model.level)
        
        # Se game over, mostra mensagem
        if model.game_over:
            self._draw_game_over()
            
        pygame.display.flip()
        
    def _draw_grid(self, grid):
        """Desenha o grid do jogo."""
        # Área do grid
        grid_left = (SCREEN_WIDTH - GRID_WIDTH * GRID_SIZE) // 2
        grid_top = (SCREEN_HEIGHT - GRID_HEIGHT * GRID_SIZE) // 2
        
        # Desenha o fundo do grid
        pygame.draw.rect(
            self.screen, GRAY,
            (grid_left - 2, grid_top - 2, 
             GRID_WIDTH * GRID_SIZE + 4, GRID_HEIGHT * GRID_SIZE + 4),
            0
        )
        
        # Desenha as células preenchidas
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if grid[y][x]:
                    pygame.draw.rect(
                        self.screen, grid[y][x],
                        (grid_left + x * GRID_SIZE, grid_top + y * GRID_SIZE,
                         GRID_SIZE, GRID_SIZE),
                        0
                    )
                    
        # Desenha as linhas do grid
        for x in range(GRID_WIDTH + 1):
            pygame.draw.line(
                self.screen, BLACK,
                (grid_left + x * GRID_SIZE, grid_top),
                (grid_left + x * GRID_SIZE, grid_top + GRID_HEIGHT * GRID_SIZE)
            )
        for y in range(GRID_HEIGHT + 1):
            pygame.draw.line(
                self.screen, BLACK,
                (grid_left, grid_top + y * GRID_SIZE),
                (grid_left + GRID_WIDTH * GRID_SIZE, grid_top + y * GRID_SIZE)
            )
            
    def _draw_piece(self, piece):
        """Desenha a peça atual."""
        grid_left = (SCREEN_WIDTH - GRID_WIDTH * GRID_SIZE) // 2
        grid_top = (SCREEN_HEIGHT - GRID_HEIGHT * GRID_SIZE) // 2
        
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen, piece['color'],
                        (grid_left + (piece['x'] + x) * GRID_SIZE,
                         grid_top + (piece['y'] + y) * GRID_SIZE,
                         GRID_SIZE, GRID_SIZE),
                        0
                    )
                    
    def _draw_next_piece(self, piece):
        """Desenha a próxima peça."""
        next_left = (SCREEN_WIDTH + GRID_WIDTH * GRID_SIZE) // 2 + 30
        next_top = (SCREEN_HEIGHT - 4 * GRID_SIZE) // 2
        
        # Título
        text = self.font.render("Próxima:", True, WHITE)
        self.screen.blit(text, (next_left, next_top - 30))
        
        # Desenha a peça
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen, piece['color'],
                        (next_left + x * GRID_SIZE,
                         next_top + y * GRID_SIZE,
                         GRID_SIZE, GRID_SIZE),
                        0
                    )
                    
    def _draw_game_info(self, score, level):
        """Desenha a pontuação e nível."""
        info_left = (SCREEN_WIDTH - GRID_WIDTH * GRID_SIZE) // 2 - 200
        info_top = (SCREEN_HEIGHT - 100) // 2
        
        # Pontuação
        score_text = self.font.render(f"Pontos: {score}", True, WHITE)
        self.screen.blit(score_text, (info_left, info_top))
        
        # Nível
        level_text = self.font.render(f"Nível: {level}", True, WHITE)
        self.screen.blit(level_text, (info_left, info_top + 30))
        
    def _draw_game_over(self):
        """Desenha a mensagem de game over."""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Semi-transparente
        self.screen.blit(overlay, (0, 0))
        
        text = self.font.render("GAME OVER - Pressione R para recomeçar", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.screen.blit(text, text_rect)