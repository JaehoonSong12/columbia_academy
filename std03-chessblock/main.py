#!/usr/bin/env python

#
# This script has been refactored based on the user's OOP design.
#
# We introduce a 'Game' class to manage the game loop, state,
# event handling, and drawing.
#
# Fixes applied:
# 1. 'Board._load_board_image' now correctly takes 'self' as an argument.
# 2. 'Board.get_rect' and 'GameObject.get_rect' now correctly use
#    'width' and 'height' parameters for pygame.Rect.
# 3. All event handlers (drag, drop, escape) are implemented.
# 4. The main loop now draws all objects correctly.
#

import pygame
import sys
import os

# --- CONSTANTS ---
ASSET_DIR = "assets"

#
# This helper isn't part of a class, but it's a good
# place to define the semi-transparent highlight color.
#
COLOR_DRAG_HIGHLIGHT = (100, 149, 237, 150) # Cornflower Blue

# === BOARD CLASS ===

class Board:
    """
    Represents the chessboard.
    It is responsible for its own dimensions and image.
    """
    def __init__(self, side_length=640, x=0, y=0):
        #
        # All dimensions are now derived from the side_length
        #
        self.x = x
        self.y = y
        self.side_length = side_length
        self.square_side_length = side_length // 8
        
        #
        # We 'cache' the image so it's only loaded from disk once.
        # 'self.image' is initialized to None.
        #
        self.image = None

    def get_length(self):
        return self.side_length

    def get_rect(self):
        """
        Returns the pygame.Rect for the board's *pixel* position and size.
        
        FIX: pygame.Rect takes (left, top, width, height)
        """
        return pygame.Rect(
            self.x, self.y,
            self.side_length, self.side_length
        )

    def get_image(self):
        """
        Public getter for the image.
        Calls the private _load_board_image method if the image
        hasn't been loaded yet (i.e., self.image is None).
        """
        if self.image is None:
            #
            # This is called 'lazy loading'. We only load the
            # image from disk the first time it's asked for.
            #
            self.image = self._load_board_image()
        return self.image

    def _load_board_image(self):
        """
        Loads and scales the main chessboard image.
        
        FIX: This method needs 'self' to access 'self.side_length'
        """
        file_path = os.path.join(ASSET_DIR, "chessboard.png")
        try:
            original_image = pygame.image.load(file_path)
            #
            # Scale the image to the board's dimensions
            #
            scaled_image = pygame.transform.scale(
                original_image, (self.side_length, self.side_length)
            )
        except FileNotFoundError:
            print(f"Error: Board image not found at {file_path}", file=sys.stderr)
            sys.exit(1)
        except pygame.error as e:
            print(f"Pygame Error: loading board image {file_path}: {e}", file=sys.stderr)
            sys.exit(1)
        return scaled_image

    def coords_to_grid(self, x, y):
        """
        Converts pixel (x, y) coordinates to grid (col, row) coordinates.
        Returns (col, row) or None if out of bounds.
        """
        #
        # Make sure the click is on the board
        #
        if not self.get_rect().collidepoint(x, y):
            return None
            
        #
        # Convert pixel coordinates to grid coordinates (0-7)
        #
        col = (x - self.x) // self.square_side_length
        row = (y - self.y) // self.square_side_length
        
        return (col, row)

# === PIECE CLASSES ===

class GameObject:
    """
    A simple class to represent game objects with position and size.
    This is the 'base class' for all pieces.
    """
    def __init__(self, x, y, side_length):
        #
        # 'x' and 'y' are now GRID coordinates (0-7)
        #
        self.x = x
        self.y = y
        
        #
        # 'side_length' is the size of the piece (e.g., 80)
        #
        self.side_length = side_length
        self.isAlive = True
        self.isScalarable = False # For your move logic (Rook, Bishop, Queen)
        self.name = ""             # e.g., "pawn", "king"
        self.image = None
        self.color = 0             # 0 for white, 1 for black
        self.movements = []

    def get_rect(self):
        """
        Returns the pygame.Rect for the piece's *pixel* position and size.
        It calculates this from its *grid* position (self.x, self.y).
        
        FIX: pygame.Rect takes (left, top, width, height)
        """
        return pygame.Rect(
            self.x * self.side_length, self.y * self.side_length,
            self.side_length, self.side_length
        )

    def get_image(self):
        """
        Public getter for the piece's image.
        Loads the image if it hasn't been loaded yet.
        """
        if self.image is None:
            self.image = self._init_image()
        return self.image

    def _init_image(self):
        """
        Loads and scales the piece's image based on its name and color.
        This is a great, clean way to handle asset loading.
        """
        color_name = "white" if self.color == 0 else "black"
        piece_name = self.name
        
        #
        # We must check for an empty name, or this will
        # try to load "white-.png" or "black-.png"
        #
        if not piece_name:
            print(f"Error: GameObject has no 'name' set.", file=sys.stderr)
            return None
            
        file_path = os.path.join(ASSET_DIR, f"{color_name}-{piece_name}.png")
        
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

#
# All your piece classes are great.
# We just need to make them accept the 'side_length'
# from the board and pass it to the 'super()' call.
#

class King(GameObject):
    def __init__(self, x, y, color, side_length):
        super().__init__(x, y, side_length)
        self.name = "king"
        self.color = color
        self.movements = [
            (0,-1), (1,-1), (1,0), (1,1),
            (0,1), (-1,1), (-1,0), (-1,-1)
        ]

class Knight(GameObject):
    def __init__(self, x, y, color, side_length):
        super().__init__(x, y, side_length)
        self.name = "knight"
        self.color = color
        self.movements = [
            (1,-2), (2,-1), (2,1), (1,2),
            (-1,2), (-2,1), (-2,-1), (-1,-2)
        ]

class Pawn(GameObject):
    def __init__(self, x, y, color, side_length):
        super().__init__(x, y, side_length)
        self.color = color
        self.name = "pawn"
        #
        # Your move logic will need to check 'self.color'
        # to know if this (0, -1) move is correct, or if
        # it should be (0, 1) for black.
        #
        self.movements = [
            (0,-1) # Assuming for White
        ]

class Queen(GameObject):
    def __init__(self, x, y, color, side_length):
        super().__init__(x, y, side_length)
        self.color = color
        self.name = "queen"
        self.isScalarable = True
        self.movements = [
            (0,-1), (1,-1), (1,0), (1,1),
            (0,1), (-1,1), (-1,0), (-1,-1),
            #
            # Note: You have some duplicate moves here,
            # which is fine, but you can simplify.
            #
        ]

class Rook(GameObject):
    def __init__(self, x, y, color, side_length):
        super().__init__(x, y, side_length)
        self.color = color
        self.name = "rook"
        self.isScalarable = True
        self.movements = [
            (1,0), (0,-1), (-1,0), (0,1)
        ]

class Bishop(GameObject):
    def __init__(self, x, y, color, side_length):
        super().__init__(x, y, side_length)
        self.color = color
        self.name = "bishop"
        self.isScalarable = True
        self.movements = [
            (1,-1), (1,1), (-1,1), (-1,-1)
        ]

# === GAME CLASS ===

class Game:
    """
    This class manages the main game loop, state,
    event handling, and drawing. It owns all the
    other objects (Board, GameObjects).
    """
    def __init__(self):
        #
        # --- 1. Initialization ---
        #
        pygame.init()
        
        #
        # --- 2. Create Objects ---
        #
        self.board = Board(side_length=640)
        self.game_objects = self._create_pieces()
        
        #
        # --- 3. Setup Display ---
        #
        WINDOW_WIDTH = self.board.get_length()
        WINDOW_HEIGHT = self.board.get_length()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pygame Chess (OOP)")
        self.clock = pygame.time.Clock()
        
        #
        # --- 4. Game State Variables ---
        #
        self.running = True
        self.selected_piece = None # This will store the 'GameObject' being dragged
        self.is_dragging = False
        self.drag_pos = (0, 0)     # The current raw (x, y) of the mouse

    def _create_pieces(self):
        """
        A helper method to create and return the initial
        list of 32 piece (GameObject) instances.
        """
        #
        # We must pass the 'square_side_length' to the pieces
        # so they know their own size.
        #
        s = self.board.square_side_length 
        
        #
        # Your 'game_objects' list was perfect.
        #
        pieces = [
            Rook(0, 0, 1, s), Knight(1, 0, 1, s), Bishop(2, 0, 1, s), Queen(3, 0, 1, s), King(4, 0, 1, s), Bishop(5, 0, 1, s), Knight(6, 0, 1, s), Rook(7, 0, 1, s),
            Pawn(0, 1, 1, s), Pawn(1, 1, 1, s), Pawn(2, 1, 1, s), Pawn(3, 1, 1, s), Pawn(4, 1, 1, s), Pawn(5, 1, 1, s), Pawn(6, 1, 1, s), Pawn(7, 1, 1, s),
            
            Pawn(0, 6, 0, s), Pawn(1, 6, 0, s), Pawn(2, 6, 0, s), Pawn(3, 6, 0, s), Pawn(4, 6, 0, s), Pawn(5, 6, 0, s), Pawn(6, 6, 0, s), Pawn(7, 6 ,0, s),
            Rook(0, 7, 0, s), Knight(1, 7, 0, s), Bishop(2, 7, 0, s), Queen(3, 7, 0, s), King(4, 7, 0, s), Bishop(5, 7, 0, s), Knight(6, 7, 0, s), Rook(7, 7, 0, s),
        ]
        return pieces

    def run(self):
        """
        This is the main game loop.
        It will continue to run as long as 'self.running' is True.
        """
        while self.running:
            #
            # --- 1. Handle Events ---
            #
            self._handle_events()
            
            #
            # --- 2. Draw Everything ---
            #
            self._draw()
            
            #
            # --- 3. Control Framerate ---
            #
            self.clock.tick(60)
            
        #
        # The loop has ended, so we quit.
        #
        pygame.quit()
        print("Game has ended. Goodbye!")
        sys.exit()

    def _handle_events(self):
        """
        Private method to process the event queue.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._cancel_drag()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    self._on_mouse_down(event)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # Left click
                    self._on_mouse_up(event)
            
            elif event.type == pygame.MOUSEMOTION:
                self._on_mouse_move(event)

    def _on_mouse_down(self, event):
        """
        Handles the MOUSEBUTTONDOWN event.
        Tries to "pick up" a piece.
        """
        x, y = event.pos
        grid_pos = self.board.coords_to_grid(x, y)
        
        if grid_pos is None:
            return # Click was off the board
            
        col, row = grid_pos
        piece = self._get_piece_at_grid(col, row)
        
        if piece is not None:
            print(f"Picked up {piece.name} at ({col}, {row})")
            self.selected_piece = piece
            self.is_dragging = True
            self.drag_pos = event.pos

    def _on_mouse_up(self, event):
        """
        Handles the MOUSEBUTTONUP event.
        "Drops" a piece, triggering your logic.
        """
        if not self.is_dragging:
            return
            
        x, y = event.pos
        grid_pos = self.board.coords_to_grid(x, y)
        
        if grid_pos is None:
            #
            # If dropped off-board, cancel the move
            #
            print("Dropped off-board. Canceling move.")
            self._cancel_drag()
            return
            
        col, row = grid_pos
        from_pos = (self.selected_piece.x, self.selected_piece.y)
        to_pos = (col, row)
        
        print(f"Dropped {self.selected_piece.name} from {from_pos} to {to_pos}")

        #
        # *** THIS IS THE HOOK FOR YOUR LOGIC ***
        #
        # Here, you would check if the move is legal
        # using 'self.selected_piece.movements', 'self.isScalarable',
        # and checking for other pieces.
        #
        # For now, we will just *make* the move,
        # and handle a simple capture.
        #
        
        # --- Simple Capture Logic ---
        target_piece = self._get_piece_at_grid(col, row)
        if target_piece is not None and target_piece != self.selected_piece:
            #
            # Make sure it's not the *same* color
            #
            if target_piece.color != self.selected_piece.color:
                print(f"Captured {target_piece.name}")
                target_piece.isAlive = False # "Kill" the piece
            else:
                #
                # Can't capture your own piece, cancel move
                #
                print("Cannot capture friendly piece. Canceling move.")
                self._cancel_drag()
                return

        #
        # --- Update Piece Position ---
        #
        self.selected_piece.x = col
        self.selected_piece.y = row
        
        #
        # Reset the game state
        #
        self._cancel_drag()

    def _on_mouse_move(self, event):
        """
        Handles the MOUSEMOTION event.
        Updates the 'drag_pos' if a piece is being dragged.
        """
        if self.is_dragging:
            self.drag_pos = event.pos

    def _cancel_drag(self):
        """
        A helper to reset the dragging state.
        """
        self.is_dragging = False
        self.selected_piece = None
        self.drag_pos = (0, 0)
        
    def _get_piece_at_grid(self, col, row):
        """
        Returns the 'GameObject' at a given grid (col, row)
        or None if no piece is there.
        """
        for piece in self.game_objects:
            if piece.x == col and piece.y == row and piece.isAlive:
                return piece
        return None

    def _draw(self):
        """
        Private method to draw the entire game screen.
        """
        
        #
        # --- 1. Draw the Board ---
        #
        self.screen.blit(self.board.get_image(), self.board.get_rect())
        
        #
        # --- 2. Draw the Pieces ---
        #
        for piece in self.game_objects:
            if not piece.isAlive:
                continue # Skip dead pieces
                
            #
            # If this piece is *not* the one being dragged,
            # draw it at its static grid position.
            #
            if not self.is_dragging or piece != self.selected_piece:
                self.screen.blit(piece.get_image(), piece.get_rect())
        
        #
        # --- 3. Draw the Dragged Piece ---
        #
        if self.is_dragging and self.selected_piece is not None:
            #
            # --- 3a. Draw Highlight Square ---
            #
            grid_pos = self.board.coords_to_grid(self.drag_pos[0], self.drag_pos[1])
            if grid_pos is not None:
                col, row = grid_pos
                highlight_rect = pygame.Rect(
                    col * self.board.square_side_length,
                    row * self.board.square_side_length,
                    self.board.square_side_length,
                    self.board.square_side_length
                )
                #
                # We create a new Surface for the highlight
                # to control its transparency (alpha).
                #
                highlight_surf = pygame.Surface(highlight_rect.size, pygame.SRCALPHA)
                highlight_surf.fill(COLOR_DRAG_HIGHLIGHT)
                self.screen.blit(highlight_surf, highlight_rect)
            
            #
            # --- 3b. Draw Piece at Mouse ---
            #
            image = self.selected_piece.get_image()
            
            #
            # Center the image on the mouse cursor
            #
            centered_x = self.drag_pos[0] - self.selected_piece.side_length // 2
            centered_y = self.drag_pos[1] - self.selected_piece.side_length // 2
            
            self.screen.blit(image, (centered_x, centered_y))
            
        #
        # --- 4. Update the Display ---
        #
        pygame.display.flip()

# === MAIN ENTRY POINT ===

def main():
    """
    Main entry point.
    Creates the Game object and calls its 'run' method.
    """
    game = Game()
    game.run()

if __name__ == "__main__":
    main()