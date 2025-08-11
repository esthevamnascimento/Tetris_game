# tetris/main.py
"""
Ponto de entrada principal do jogo Tetris.

Orquestra a interação entre Model, View e Controller.
"""
import pygame
import time
from model import TetrisModel
from view import TetrisView
from controller import TetrisController

def main():
    """Função principal que inicia e executa o jogo."""
    model = TetrisModel()
    view = TetrisView()
    controller = TetrisController(model)
    
    running = True
    last_time = time.time()
    
    while running:
        # Calcula delta time
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time
        
        # Atualiza e desenha
        running = controller.handle_events()
        model.update(delta_time)
        view.draw(model)
        
        # Controla FPS
        view.clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()