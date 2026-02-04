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
    [[1, 1, 1, 1]],  # I shape
    [[1, 1, 1], [0, 0, 1]],  # L shape
    [[1, 1, 1], [1, 0, 0]],  # J shape
    [[1, 1], [1, 1]],  # O shape
    [[0, 1, 1], [1, 1, 0]],  # S shape
    [[1, 1, 1], [0, 1, 0]],  # T shape
    [[1, 1, 0], [0, 1, 1]],  # Z shape
]

class Tetris:
    def __init__(self):
        self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.current_piece = self.new_piece()
        self.current_pos = [0, BOARD_WIDTH // 2]  # Starting position

    def new_piece(self):
        return random.choice(SHAPES)

    def rotate_piece(self):
        self.current_piece = list(zip(*self.current_piece[::-1]))  # Rotate 90 degrees

    def collision(self, offset):
        # Check for collisions with walls and other blocks
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    board_x = self.current_pos[1] + x + offset[1]
                    board_y = self.current_pos[0] + y + offset[0]
                    if (board_x < 0 or board_x >= BOARD_WIDTH or board_y >= BOARD_HEIGHT or
                        (board_y >= 0 and self.board[board_y][board_x])):
                        return True
        return False

    def join_matrixes(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_pos[0] + y][self.current_pos[1] + x] = 1

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(row)]
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [0] * BOARD_WIDTH)

    def update(self):
        if self.collision((1, 0)):
            self.join_matrixes()
            self.clear_lines()
            self.current_piece = self.new_piece()
            self.current_pos = [0, BOARD_WIDTH // 2]
        else:
            self.current_pos[0] += 1

    def draw(self, screen):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                color = COLORS[cell] if cell else BLACK
                pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

        # Draw the current piece
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, COLORS[0], ((self.current_pos[1] + x) * BLOCK_SIZE,
                                                          (self.current_pos[0] + y) * BLOCK_SIZE,
                                                          BLOCK_SIZE, BLOCK_SIZE))


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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not tetris.collision((0, -1)):
                        tetris.current_pos[1] -= 1
                elif event.key == pygame.K_RIGHT:
                    if not tetris.collision((0, 1)):
                        tetris.current_pos[1] += 1
                elif event.key == pygame.K_DOWN:
                    tetris.current_pos[0] += 1
                elif event.key == pygame.K_UP:
                    tetris.rotate_piece()

        tetris.update()
        screen.fill(BLACK)
        tetris.draw(screen)
        pygame.display.flip()
        clock.tick(10)


if __name__ == '__main__':
    main()