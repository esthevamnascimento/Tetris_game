# tetris/controller.py
"""
Módulo Controller do jogo Tetris.

Responsável por:
- Capturar entrada do usuário
- Traduzir para ações no jogo
- Gerenciar eventos
"""
import pygame

class TetrisController:
    def __init__(self, model):
        """Inicializa o controlador com referência ao modelo."""
        self.model = model
        
    def handle_events(self):
        """Processa todos os eventos e atualiza o modelo conforme necessário.
        
        Retorna:
            False se o usuário quer sair, True caso contrário.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.KEYDOWN:
                if not self.model.game_over:
                    if event.key == pygame.K_LEFT:
                        self.model.move_piece(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.model.move_piece(1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.model.move_piece(0, 1)
                    elif event.key == pygame.K_UP:
                        self.model.rotate_piece()
                    elif event.key == pygame.K_SPACE:
                        # Hard drop (cai até o fundo)
                        while self.model.move_piece(0, 1):
                            pass
                # Reset do jogo
                if event.key == pygame.K_r:
                    self.model.reset_game()
                    
        return True