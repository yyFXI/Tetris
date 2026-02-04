import pygame
import random

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
BOARD_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
BOARD_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (128, 0, 128),  # Purple
    (255, 0, 0),    # Red
]

# Shapes
SHAPES = [
    [['.....',
      '.....',
      '..X..',
      '..X..',
      '.....'],
    
     ['.....',
      '.....',
      'XXXXX',
      '.....',
      '.....']],

    [['.....',
      '.....',
      'XX..X',
      '.....',
      '.....'],
    
     ['.....',
      'X....',
      'XXX..',
      '.....',
      '.....']],

    [['.....',
      '.....',
      '.XX..',
      '..X..',
      '..X..'],
    
     ['.....',
      '..X..',
      '..XX.',
      '.....',
      '.....']],
    
    [['.....',
      '.....',
      '..X..',
      '..XX.',
      '.....'],
    
     ['.....',
      '.X...',
      '.XX..',
      '.....',
      '.....']],

    # Add other shapes similarly...
]

class Tetris:
    def __init__(self):
        self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.current_piece = None
        self.next_piece = self.new_piece()
        self.score = 0
        self.game_over = False

    def new_piece(self):
        return SHAPES[random.randint(0, len(SHAPES) - 1)]

    def rotate_piece(self):
        self.current_piece = self.current_piece[1:] + self.current_piece[:1]  # Simple rotation

    def collision(self, offset):
        # Check for collisions with walls and other blocks
        return False

    def clear_lines(self):
        # Check for completed lines, clear them, and increase score
        self.score += 1

    def update(self):
        if not self.game_over:
            # Game update logic
            pass

    def draw(self, screen):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                color = COLORS[cell] if cell else BLACK
                pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')
    clock = pygame.time.Clock()
    tetris = Tetris()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        tetris.update()
        screen.fill(BLACK)
        tetris.draw(screen)
        pygame.display.flip()
        clock.tick(10)  # Adjust the speed of the game


if __name__ == '__main__':
    main()