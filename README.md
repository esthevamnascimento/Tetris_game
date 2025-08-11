# 🎮 Tetris em Python com PyGame

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org/)

Implementação do clássico jogo Tetris desenvolvido em Python utilizando a biblioteca PyGame, seguindo princípios de Clean Code e arquitetura MVC (Model-View-Controller).

## 📋 Índice
- [Funcionalidades](#✨-funcionalidades)
- [Tecnologias](#🛠-tecnologias)
- [Como Executar](#▶-como-executar)
- [Estrutura do Projeto](#📂-estrutura-do-projeto)
- [Desafios Encontrados](#⚠️-desafios-encontrados)
- [Melhorias Futuras](#🚀-melhorias-futuras)
- [Licença](#📝-licença)

## ✨ Funcionalidades
✔️ Sistema completo de peças Tetris com rotação  
✔️ Colisão e movimentação suave  
✔️ Sistema de pontuação progressivo  
✔️ Aumento de dificuldade por nível  
✔️ Visualização da próxima peça  
✔️ Tela de Game Over  
✔️ Controles intuitivos (setas e espaço)  

## 🛠 Tecnologias
- **Python 3.8+** - Linguagem principal
- **Pygame** - Biblioteca para desenvolvimento de jogos
- **POO** - Programação Orientada a Objetos
- **Arquitetura MVC** - Separação clara de responsabilidades

## ▶ Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- Pip instalado

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/esthevamnascimento/Tetris_game.git
cd Tetris_game 
```

###2.Instale as dependências:
```bash
pip install pygame
```

###3.Execute o jogo:
```bash
python -m tetris_game.main
```

###Controles:
```bash
← → : Movimento horizontal

↓ : Acelera a queda

↑ : Rotaciona a peça

Espaço : Drop instantâneo

R : Reinicia o jogo
```

###📂 Estrutura do Projeto

```bash
tetris_game/
├── __init__.py
├── constants.py    # Configurações e constantes do jogo
├── controller.py   # Lógica de controle e inputs
├── model.py        # Regras e estado do jogo
├── view.py         # Renderização gráfica
└── main.py         # Ponto de entrada do programa
```

###⚠️ Desafios Encontrados

1. Problemas de Importação
Desafio: Dificuldade em configurar as importações entre módulos

Solução: Implementação de:

```bash
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
```

2. Rotação de Peças
Desafio: Lógica complexa para rotacionar peças sem sair dos limites

Solução: Matriz de rotação com verificação de colisão:

```bash
def rotate_piece(self):
    rotated = [list(row)[::-1] for row in zip(*self.current_piece['shape'])]
    # Verificação de colisão após rotação
```

###3. Sistema de Pontuação

Desafio: Criar progressão balanceada

Solução: Pontuação exponencial por linhas completadas:

```bash
SCORE_DATA = {1: 100, 2: 300, 3: 500, 4: 800}
```

###🚀 Melhorias Futuras

-Adicionar menu inicial

-Implementar sistema de highscore

-Adicionar efeitos sonoros

-Criar sistema de peças especiais

-Desenvolver versão multiplayer

📝 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

Desenvolvido com ❤️ por Esthevam Nascimento
