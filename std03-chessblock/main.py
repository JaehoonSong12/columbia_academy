#!/usr/bin/env python

#
# A foundational Pygame script for a chess UI.
#
# This version is updated to:
# 1. Use more descriptive asset filenames (e.g., 'white-pawn.png').
# 2. Use a single 'chessboard.png' image for the board background.
#

import pygame
import chess
import sys
import os # Added 'os' to help construct file paths

# === CONSTANTS ===

# --- Window and Board Dimensions ---
# SQUARE_SIZE is still the "source of truth" for all dimensions.



# --- Colors ---
# We only need the highlight color now.
COLOR_DRAG_HIGHLIGHT = (100, 149, 237, 150) # Cornflower Blue, semi-transparent

# --- Asset Paths ---
# This is now just a reference to the folder.

# --- Mappings for New Filenames ---
# These dicts will help us build the new filenames
# from the 'python-chess' piece data.
PIECE_NAME_MAP = {
    'p': 'pawn', 'n': 'knight', 'b': 'bishop',
    'r': 'rook', 'q': 'queen', 'k': 'king'
}

COLOR_NAME_MAP = {
    chess.WHITE: 'white',
    chess.BLACK: 'black'
}


















def square_to_coords(square):
    """
    Converts a 'python-chess' square index (0-63) to Pygame (x, y) coordinates.
    """
    file = chess.square_file(square)
    rank = chess.square_rank(square)
    x = file * SQUARE_SIZE
    y = (7 - rank) * SQUARE_SIZE # Flip the y-axis
    return (x, y)

def coords_to_square(x, y):
    """
    Converts Pygame (x, y) coordinates back to a 'python-chess' square index.
    """
    if x < 0 or x >= BOARD_WIDTH or y < 0 or y >= BOARD_HEIGHT:
        return None # Out of bounds
        
    file = x // SQUARE_SIZE
    rank = 7 - (y // SQUARE_SIZE) # Invert the y-coordinate
    
    return chess.square(file, rank)

# === DRAWING FUNCTIONS ===

#
# *** The 'draw_board' function is no longer needed! ***
# We will draw the board image directly.
#

def draw_pieces(screen, board, piece_images, selected_square, is_dragging):
    """
    Draws all pieces from the 'python-chess' board object onto the screen.
    
    If a piece is being dragged, we skip drawing it at its 'selected_square'.
    This function *did not need to change* because 'load_piece_images'
    still creates a dictionary keyed by the piece symbols.
    """
    for square in chess.SQUARES:
        if is_dragging and square == selected_square:
            continue
            
        piece = board.piece_at(square)
        if piece is not None:
            symbol = piece.symbol()
            image = piece_images[symbol]
            x, y = square_to_coords(square)
            screen.blit(image, (x, y))

def draw_drag(screen, piece_images, dragged_piece_data):
    """
    Draws the currently dragged piece and a highlight square.
    This function also did not need to change.
    """
    if dragged_piece_data is None:
        return
        
    # Draw highlight on the square under the mouse
    mouse_x, mouse_y = dragged_piece_data["pos"]
    hovered_square = coords_to_square(mouse_x, mouse_y)
    
    if hovered_square is not None:
        highlight = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
        highlight.fill(COLOR_DRAG_HIGHLIGHT)
        x, y = square_to_coords(hovered_square)
        screen.blit(highlight, (x, y))
        
    # Draw the piece centered on the mouse
    symbol = dragged_piece_data["symbol"]
    image = piece_images[symbol]
    centered_x = mouse_x - SQUARE_SIZE // 2
    centered_y = mouse_y - SQUARE_SIZE // 2
    screen.blit(image, (centered_x, centered_y))


# === MAIN GAME FUNCTION ===

# def main():
#     """
#     Main entry point. Initializes Pygame, loads assets, and runs the game loop.
#     """
    
#     # --- 1. Initialization ---
#     pygame.init()
#     screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#     pygame.display.set_caption("Pygame Chess")
#     clock = pygame.time.Clock()
    
#     # --- 2. Load Assets ---
#     # We now call our two new loading functions
#     board_image = load_board_image()
#     piece_images = load_piece_images()

#     # --- 3. Initialize Game State ---
#     board = chess.Board() # The "brain"
    
#     # --- 4. Game Loop Variables (State) ---
#     running = True
#     selected_square = None
#     is_dragging = False
#     dragged_piece_data = None

#     # --- 5. Main Game Loop ---
#     while running:
        
#         # --- 6. Event Handling (No changes here) ---
#         for event in pygame.event.get():
            
#             if event.type == pygame.QUIT:
#                 running = False
            
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     selected_square = None
#                     is_dragging = False
#                     dragged_piece_data = None
            
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     x, y = event.pos
#                     clicked_square = coords_to_square(x, y)
                    
#                     if clicked_square is not None:
#                         piece = board.piece_at(clicked_square)
#                         if piece is not None:
#                             selected_square = clicked_square
#                             is_dragging = True
#                             dragged_piece_data = {
#                                 "symbol": piece.symbol(),
#                                 "pos": event.pos
#                             }

#             elif event.type == pygame.MOUSEBUTTONUP:
#                 if event.button == 1 and is_dragging:
#                     x, y = event.pos
#                     dropped_square = coords_to_square(x, y)
                    
#                     print(f"Drag from {chess.square_name(selected_square)} to {chess.square_name(dropped_square) if dropped_square else 'None'}")

#                     #
#                     # *** YOUR LOGIC HOOK ***
#                     # Implement your move validation and 'board.push()' here.
#                     #
                    
#                     # Reset dragging state
#                     selected_square = None
#                     is_dragging = False
#                     dragged_piece_data = None

#             elif event.type == pygame.MOUSEMOTION:
#                 if is_dragging and dragged_piece_data is not None:
#                     dragged_piece_data["pos"] = event.pos

#         # --- 7. Drawing (This section is simplified) ---
        
#         # Step 1: Draw the background board image
#         # This replaces the old 'draw_board(screen)' call.
#         screen.blit(board_image, (0, 0))
        
#         # Step 2: Draw the pieces on the board
#         draw_pieces(screen, board, piece_images, selected_square, is_dragging)
        
#         # Step 3: Draw the dragged piece (if any)
#         if is_dragging and dragged_piece_data is not None:
#             draw_drag(screen, piece_images, dragged_piece_data)

#         # --- 8. Update the Display ---
#         pygame.display.flip()

#         # --- 9. Control Framerate ---
#         clock.tick(60)

#     # --- 10. Quit ---
#     pygame.quit()
#     print("Game has ended. Goodbye!")

















































ASSET_DIR = "assets"



class Board: 
    """
    A simple class to represent the chessboard.
    This class is not strictly necessary for the current implementation,
    but it can be useful for future extensions.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.side_length = 640
        self.image = None
    
    def get_length(self):
        return self.side_length

    def get_rect(self):
        return pygame.Rect(
            self.x, self.y, 
            self.x + self.side_length, self.y + self.side_length
        )
    
    def get_image(self):
        if not hasattr(self, 'image'):
            self.image = self._load_board_image()
        return self.image
    
    def _load_board_image():
        """
        Loads and scales the main chessboard image.
        """
        file_path = os.path.join(ASSET_DIR, "chessboard.png")
        try:
            # Load the original image
            original_image = pygame.image.load(file_path)
            # Scale it to fit our defined board dimensions
            scaled_image = pygame.transform.scale(original_image, (self.side_length, self.side_length))
        except FileNotFoundError:
            print(f"Error: Board image not found at {file_path}", file=sys.stderr)
            sys.exit(1)
        except pygame.error as e:
            print(f"Pygame Error: loading board image {file_path}: {e}", file=sys.stderr)
            sys.exit(1)
        return scaled_image



class GameObject:
    """
    A simple class to represent game objects with position and size.
    This class is not strictly necessary for the current implementation,
    but it can be useful for future extensions.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.side_length = 80
        self.isAlive = True
        self.isScalarable = False
        self.name = ""
        self.image = None
        self.color = 0 # 0 for white, 1 for black
        self.movements = []

    def get_rect(self):
        return pygame.Rect(
            self.x * self.side_length, self.y * self.side_length, 
            (self.x + 1) * self.side_length, (self.y + 1) * self.side_length
        )
    
    def get_image(self):
        if self.image is None:
            self.image = self._init_image()
        return self.image
    
    def _init_image(self):
        color_name = "white" if self.color == 0 else "black"
        piece_name = self.name
        file_path = os.path.join(ASSET_DIR, f"{color_name}-{piece_name}.png")
        # Load and scale the image, handling errors
        try:
            image = pygame.image.load(file_path)
            scaled_image = pygame.transform.smoothscale(image, (self.side_length, self.side_length))
        except FileNotFoundError:
            print(f"Error: Asset not found at {file_path}", file=sys.stderr)
            sys.exit(1)
        except pygame.error as e:
            print(f"Pygame Error: loading image {file_path}: {e}", file=sys.stderr)
            sys.exit(1)
        return scaled_image





class King(GameObject):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.name = "king"
        self.color = color
        self.movements = [
            (0,-1), (1,-1), (1,0), (1,1),
            (0,1), (-1,1), (-1,0), (-1,-1)
        ]

class Knight(GameObject):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.name = "knight"
        self.color = color
        self.movements = [
            (1,-2), (2,-1), (2,1), (1,2),
            (-1,2), (-2,1), (-2,-1), (-1,-2)
        ]

class Pawn(GameObject):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color
        self.name = "pawn"
        self.movements = [
            (0,-1)
        ]


class Queen(GameObject):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color
        self.name = "queen"
        self.isScalarable = True
        self.movements = [
            (0,-1), (1,-1), (1,0), (1,1),
            (0,1), (-1,1), (-1,0), (-1,-1),
            (1,-0), (0,-1), (-1,0), (0,1)
        ]

class Rook(GameObject):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color
        self.name = "rook"
        self.isScalarable = True
        self.movements = [
            (1,0), (0,-1), (-1,0), (0,1)
        ]

class Bishop(GameObject):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color
        self.name = "bishop"
        self.isScalarable = True
        self.movements = [
            (1,-1), (1,1), (-1,1), (-1,-1)
        ]



def main():
    """
    Main entry point. Initializes Pygame, loads assets, and runs the game loop.
    """
    # --- 1. Initialization ---
    pygame.init()

    board = Board()
    game_objects = [
        Rook(0, 0, 1), Knight(1, 0, 1), Bishop(2, 0, 1), Queen(3, 0, 1), King(4, 0, 1), Bishop(5, 0, 1), Knight(6, 0, 1), Rook(7, 0, 1),
        Pawn(0, 1, 1), Pawn(1, 1, 1), Pawn(2, 1, 1), Pawn(3, 1, 1), Pawn(4, 1, 1), Pawn(5, 1, 1), Pawn(6, 1, 1), Pawn(7, 1, 1),
        
        Pawn(0, 6, 0), Pawn(1, 6, 0), Pawn(2, 6, 0), Pawn(3, 6, 0), Pawn(4, 6, 0), Pawn(5, 6, 0), Pawn(6, 6, 0), Pawn(7, 6 ,0),
        Rook(0, 7, 0), Knight(1, 7, 0), Bishop(2, 7, 0), Queen(3, 7, 0), King(4, 7, 0), Bishop(5, 7, 0), Knight(6, 7, 0), Rook(7, 7, 0),
    ]

    
    WINDOW_WIDTH = board.get_length()
    WINDOW_HEIGHT = board.get_length()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pygame Chess")
    clock = pygame.time.Clock()
    
    
    # --- 4. Game Loop Variables (State) ---
    running = True
    selected_square = None
    is_dragging = False
    dragged_piece_data = None

    # --- 5. Main Game Loop ---
    while running:
        
        # --- 6. Event Handling (No changes here) ---
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    selected_square = None
                    is_dragging = False
                    dragged_piece_data = None
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    clicked_square = coords_to_square(x, y)
                    
                    if clicked_square is not None:
                        piece = board.piece_at(clicked_square)
                        if piece is not None:
                            selected_square = clicked_square
                            is_dragging = True
                            dragged_piece_data = {
                                "symbol": piece.symbol(),
                                "pos": event.pos
                            }

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and is_dragging:
                    x, y = event.pos
                    dropped_square = coords_to_square(x, y)
                    
                    print(f"Drag from {chess.square_name(selected_square)} to {chess.square_name(dropped_square) if dropped_square else 'None'}")

                    #
                    # *** YOUR LOGIC HOOK ***
                    # Implement your move validation and 'board.push()' here.
                    #
                    
                    # Reset dragging state
                    selected_square = None
                    is_dragging = False
                    dragged_piece_data = None

            elif event.type == pygame.MOUSEMOTION:
                if is_dragging and dragged_piece_data is not None:
                    dragged_piece_data["pos"] = event.pos

        # ---









if __name__ == "__main__":
    main()

