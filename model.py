# tetris/model.py
"""
Módulo Model do jogo Tetris.

Responsável pela lógica do jogo:
- Estado do tabuleiro
- Movimento das peças
- Colisões
- Pontuação
- Regras do jogo
"""
import random
from typing import List, Tuple, Optional
from constants import GRID_WIDTH, GRID_HEIGHT, SHAPES, COLORS, INITIAL_SPEED, SPEED_INCREASE

class TetrisModel:
    def __init__(self):
        """Inicializa o modelo do jogo Tetris."""
        self.reset_game()
        
    def reset_game(self):
        """Reseta o estado do jogo para o inicial."""
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self._new_piece()
        self.next_piece = self._new_piece()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.speed = INITIAL_SPEED
        self.time_since_last_move = 0.0
        
    def _new_piece(self) -> dict:
        """Gera uma nova peça aleatória.
        
        Retorna:
            Um dicionário com: shape, cor, posição (x, y) e rotação.
        """
        shape_idx = random.randint(0, len(SHAPES) - 1)
        return {
            'shape': SHAPES[shape_idx],
            'color': COLORS[shape_idx],
            'x': GRID_WIDTH // 2 - len(SHAPES[shape_idx][0]) // 2,
            'y': 0,
            'rotation': 0
        }
        
    def rotate_piece(self):
        """Rotaciona a peça atual se possível."""
        if self.game_over:
            return
            
        rotated = []
        # Transpõe a matriz da peça para rotacionar
        for i in range(len(self.current_piece['shape'][0])):
            new_row = []
            for j in range(len(self.current_piece['shape']) - 1, -1, -1):
                new_row.append(self.current_piece['shape'][j][i])
            rotated.append(new_row)
            
        old_shape = self.current_piece['shape']
        self.current_piece['shape'] = rotated
        
        # Se a rotação causar colisão, desfaz
        if self._check_collision():
            self.current_piece['shape'] = old_shape
            
    def move_piece(self, dx: int, dy: int) -> bool:
        """Move a peça atual na direção especificada.
        
        Args:
            dx: Deslocamento horizontal (-1 esquerda, 1 direita)
            dy: Deslocamento vertical (geralmente 0 ou 1)
            
        Retorna:
            True se o movimento foi válido, False caso contrário.
        """
        if self.game_over:
            return False
            
        self.current_piece['x'] += dx
        self.current_piece['y'] += dy
        
        if self._check_collision():
            # Desfaz o movimento se houver colisão
            self.current_piece['x'] -= dx
            self.current_piece['y'] -= dy
            
            # Se o movimento foi para baixo, fixa a peça
            if dy > 0:
                self._place_piece()
                self._clear_lines()
                self.current_piece = self.next_piece
                self.next_piece = self._new_piece()
                
                # Verifica se a nova peça já colide (game over)
                if self._check_collision():
                    self.game_over = True
                    
            return False
            
        return True
        
    def _check_collision(self) -> bool:
        """Verifica se a peça atual colide com algo.
        
        Retorna:
            True se há colisão, False caso contrário.
        """
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    # Calcula posição no grid
                    grid_x = self.current_piece['x'] + x
                    grid_y = self.current_piece['y'] + y
                    
                    # Verifica limites e colisões
                    if (grid_x < 0 or grid_x >= GRID_WIDTH or 
                        grid_y >= GRID_HEIGHT or 
                        (grid_y >= 0 and self.grid[grid_y][grid_x])):
                        return True
        return False
        
    def _place_piece(self):
        """Fixa a peça atual no grid."""
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    grid_y = self.current_piece['y'] + y
                    grid_x = self.current_piece['x'] + x
                    if 0 <= grid_y < GRID_HEIGHT and 0 <= grid_x < GRID_WIDTH:
                        self.grid[grid_y][grid_x] = self.current_piece['color']
                        
    def _clear_lines(self):
        """Remove linhas completas e atualiza a pontuação."""
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_cleared += 1
                # Move todas as linhas acima para baixo
                for y2 in range(y, 0, -1):
                    self.grid[y2] = self.grid[y2-1][:]
                self.grid[0] = [0 for _ in range(GRID_WIDTH)]
                
        # Atualiza pontuação
        if lines_cleared > 0:
            self.score += self._calculate_score(lines_cleared)
            self.level = self.score // 1000 + 1
            self.speed = INITIAL_SPEED * (SPEED_INCREASE ** (self.level - 1))
            
    def _calculate_score(self, lines: int) -> int:
        """Calcula a pontuação baseada no número de linhas removidas.
        
        Args:
            lines: Número de linhas removidas (1-4)
            
        Retorna:
            Pontos ganhos.
        """
        return {1: 100, 2: 300, 3: 500, 4: 800}.get(lines, 0) * self.level
        
    def update(self, delta_time: float):
        """Atualiza o estado do jogo.
        
        Args:
            delta_time: Tempo desde a última atualização em segundos.
        """
        if self.game_over:
            return
            
        self.time_since_last_move += delta_time
        if self.time_since_last_move >= self.speed:
            self.time_since_last_move = 0
            self.move_piece(0, 1)