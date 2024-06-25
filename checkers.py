import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SQUARE_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BEIGE = (245, 245, 220)
RED = (255, 0, 0)

# Create the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

LIGHT_SQUARE_IMAGE_PATH = os.path.join("images", "BeigeWood.jpg")
DARK_SQUARE_IMAGE_PATH = os.path.join("images", "BrownWood.jpg")

light_square_image = pygame.image.load(LIGHT_SQUARE_IMAGE_PATH)
dark_square_image = pygame.image.load(DARK_SQUARE_IMAGE_PATH)

# Scale the square images to match the square size
light_square_image = pygame.transform.scale(light_square_image, (SQUARE_SIZE, SQUARE_SIZE))
dark_square_image = pygame.transform.scale(dark_square_image, (SQUARE_SIZE, SQUARE_SIZE))

# Constants for circle radius and colors
CIRCLE_RADIUS = SQUARE_SIZE // 2 - 10  # Radius for the checker circles

# Create the pieces dictionary
pieces = {
    (0, 1): "black",
    (0, 3): "black",
    (0, 5): "black",
    (0, 7): "black",
    (1, 0): "black",
    (1, 2): "black",
    (1, 4): "black",
    (1, 6): "black",
    (2, 1): "black",
    (2, 3): "black",
    (2, 5): "black",
    (2, 7): "black",
    (5, 0): "red",
    (5, 2): "red",
    (5, 4): "red",
    (5, 6): "red",
    (6, 1): "red",
    (6, 3): "red",
    (6, 5): "red",
    (6, 7): "red",
    (7, 0): "red",
    (7, 2): "red",
    (7, 4): "red",
    (7, 6): "red",
}

# Draw the checkerboard
def draw_board():
    for row in range(8):
        for col in range(8):
            square_image = light_square_image if (row + col) % 2 == 0 else dark_square_image
            screen.blit(square_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Draw the checker pieces on the board

BLACK_PIECE_IMAGE_PATH = os.path.join("images", "BlackChecker.png")
RED_PIECE_IMAGE_PATH = os.path.join("images", "WhiteChecker.png")

# Load the images
black_piece_image = pygame.image.load(BLACK_PIECE_IMAGE_PATH)
red_piece_image = pygame.image.load(RED_PIECE_IMAGE_PATH)

# Scale the images to match the square size
black_piece_image = pygame.transform.scale(black_piece_image, (SQUARE_SIZE, SQUARE_SIZE))
red_piece_image = pygame.transform.scale(red_piece_image, (SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for row in range(8):
        for col in range(8):
            piece = pieces.get((row, col))
            if piece == "black":
                pygame.draw.circle(screen, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS)
                screen.blit(black_piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif piece == "red":
                pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS)
                screen.blit(red_piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Main game loop
def move_piece(start_pos, end_pos):
    piece = pieces[start_pos]
    del pieces[start_pos]
    pieces[end_pos] = piece

def handle_piece_movement(start_pos, clicked_piece):
    row, col = start_pos
    new_row, new_col = clicked_piece

    # Define the valid diagonal moves (e.g., for black pieces moving down and for red pieces moving up)
    valid_moves = [(row + 1, col + 1), (row + 1, col - 1)]  # Modify this for your specific rules

    if (new_row, new_col) in valid_moves and (new_row, new_col) not in pieces:
        move_piece(start_pos, (new_row, new_col))

def get_clicked_piece(mouse_pos):
    for (row, col), color in pieces.items():
        piece_x = col * SQUARE_SIZE
        piece_y = row * SQUARE_SIZE
        if piece_x < mouse_pos[0] < piece_x + SQUARE_SIZE and piece_y < mouse_pos[1] < piece_y + SQUARE_SIZE:
            return (row, col)
    return None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            clicked_piece = get_clicked_piece(mouse_pos)
            if clicked_piece:  # Indentation error might be related to this line
                handle_piece_movement(clicked_piece, start_pos)
                # Handle the piece movement here based on valid moves
                # Check if the move is valid and update the `pieces` dictionary
                # Redraw the board after the move
    draw_board()
    draw_pieces()
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
