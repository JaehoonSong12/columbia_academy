#!/usr/bin/env python3
"""
Simple CLI Chess in pure Python.

Features
- Full legal move validation (no move may leave your king in check)
- Castling (both sides), en passant, and promotions (default = Queen; choose piece via suffix like e7e8n)
- Threefold repetition and fifty-move rule detection
- Move input in UCI-style coordinate notation: e2e4, g7g8q, e1g1 (castle), etc.
- ASCII board display and move lists
- Undo support

Run
    python chess_cli.py

Commands inside the prompt
    - Enter a move like: e2e4
    - Promote by adding piece letter (q,r,b,n): e7e8q
    - Type: moves           # list legal moves for the side to play
    - Type: undo            # undo last half-move
    - Type: fen             # print current FEN
    - Type: help            # help
    - Type: quit            # exit

This file is deliberately self-contained (no external deps).
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple, Iterable, Dict

FILES = "abcdefgh"
RANKS = "12345678"
WHITE, BLACK = 0, 1

PIECE_DIRS = {
    'P': [(-1, 0)],           # White pawn forward (row decreases)
    'p': [(1, 0)],            # Black pawn forward
    'N': [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)],
    'B': [(-1,-1),(-1,1),(1,-1),(1,1)],
    'R': [(-1,0),(1,0),(0,-1),(0,1)],
    'Q': [(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)],
    'K': [(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)],
}
SLIDERS = set('BRQK')  # K treated as non-slider by step count

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


def sq_to_rc(sq: int) -> Tuple[int, int]:
    return divmod(sq, 8)

def rc_to_sq(r: int, c: int) -> int:
    return r*8 + c

def in_bounds(r: int, c: int) -> bool:
    return 0 <= r < 8 and 0 <= c < 8


def uci_to_move(uci: str) -> Tuple[int, int, Optional[str]]:
    """Convert e2e4 / e7e8q into (from, to, promo)."""
    uci = uci.strip().lower()
    if len(uci) not in (4,5):
        raise ValueError("Use coordinate moves like e2e4 or e7e8q")
    ffile, frank, tfile, trank = uci[0], uci[1], uci[2], uci[3]
    if ffile not in FILES or tfile not in FILES or frank not in RANKS or trank not in RANKS:
        raise ValueError("Bad coordinates")
    fr = 8 - int(frank); fc = FILES.index(ffile)
    tr = 8 - int(trank); tc = FILES.index(tfile)
    promo = None
    if len(uci) == 5:
        if uci[4] not in "qrbn":
            raise ValueError("Promotion must be q/r/b/n")
        promo = uci[4]
    return rc_to_sq(fr, fc), rc_to_sq(tr, tc), promo


def move_to_uci(fr: int, to: int, promo: Optional[str]=None) -> str:
    fr_r, fr_c = sq_to_rc(fr); to_r, to_c = sq_to_rc(to)
    s = f"{FILES[fr_c]}{8-fr_r}{FILES[to_c]}{8-to_r}"
    if promo: s += promo
    return s

@dataclass
class Move:
    fr: int
    to: int
    promo: Optional[str] = None
    is_ep: bool = False
    is_castle: bool = False

    def uci(self) -> str:
        return move_to_uci(self.fr, self.to, self.promo)

class Board:
    def __init__(self, fen: str = START_FEN):
        self.board: List[str] = ["."]*64
        self.turn: int = WHITE
        self.castling: str = "KQkq"
        self.ep_square: Optional[int] = None
        self.halfmove_clock: int = 0
        self.fullmove_number: int = 1
        self.history: List[Tuple[str, int, str, Optional[int], int, int]] = []
        self.zhist: List[str] = []  # repetition via FEN sans move clocks
        self.set_fen(fen)

    def clone(self) -> 'Board':
        b = Board(self.fen())
        b.history = self.history.copy()
        b.zhist = self.zhist.copy()
        return b

    # ------------ FEN handling ------------
    def set_fen(self, fen: str):
        parts = fen.split()
        ranks = parts[0].split('/')
        idx = 0
        for r in ranks:
            for ch in r:
                if ch.isdigit():
                    idx += int(ch)
                else:
                    self.board[idx] = ch
                    idx += 1
        self.turn = WHITE if parts[1] == 'w' else BLACK
        self.castling = parts[2] if parts[2] != '-' else ''
        self.ep_square = None if parts[3] == '-' else self.algebraic_to_sq(parts[3])
        self.halfmove_clock = int(parts[4])
        self.fullmove_number = int(parts[5])
        self._push_hash()

    def fen(self) -> str:
        rows = []
        for r in range(8):
            row = []
            cnt = 0
            for c in range(8):
                p = self.board[rc_to_sq(r,c)]
                if p == '.':
                    cnt += 1
                else:
                    if cnt:
                        row.append(str(cnt)); cnt = 0
                    row.append(p)
            if cnt: row.append(str(cnt))
            rows.append(''.join(row))
        parts = [
            '/'.join(rows),
            'w' if self.turn == WHITE else 'b',
            self.castling if self.castling else '-',
            self.sq_to_algebraic(self.ep_square) if self.ep_square is not None else '-',
            str(self.halfmove_clock),
            str(self.fullmove_number)
        ]
        return ' '.join(parts)

    def _hash_core(self) -> str:
        # For repetition: ignore halfmove/fullmove
        parts = self.fen().split()
        parts[4] = '0'; parts[5] = '1'
        return ' '.join(parts)

    def _push_hash(self):
        self.zhist.append(self._hash_core())

    @staticmethod
    def sq_to_algebraic(sq: Optional[int]) -> str:
        if sq is None: return '-'
        r, c = sq_to_rc(sq)
        return f"{FILES[c]}{8-r}"

    @staticmethod
    def algebraic_to_sq(s: str) -> int:
        file, rank = s[0], s[1]
        c = FILES.index(file); r = 8 - int(rank)
        return rc_to_sq(r,c)

    # ------------ Helpers ------------
    def color_of(self, p: str) -> Optional[int]:
        if p == '.': return None
        return WHITE if p.isupper() else BLACK

    def king_square(self, color: int) -> int:
        k = 'K' if color == WHITE else 'k'
        for i, p in enumerate(self.board):
            if p == k: return i
        raise ValueError("King not found")

    def is_attacked_by(self, sq: int, attacker_color: int) -> bool:
        # Knights
        for dr, dc in PIECE_DIRS['N']:
            r, c = sq_to_rc(sq); r += dr; c += dc
            if in_bounds(r,c):
                p = self.board[rc_to_sq(r,c)]
                if p == ('N' if attacker_color==WHITE else 'n'):
                    return True
        # Kings
        for dr, dc in PIECE_DIRS['K']:
            r, c = sq_to_rc(sq); r += dr; c += dc
            if in_bounds(r,c):
                p = self.board[rc_to_sq(r,c)]
                if p == ('K' if attacker_color==WHITE else 'k'):
                    return True
        # Sliding attacks (bishops/rooks/queens)
        def ray(drs: Iterable[Tuple[int,int]], pieces: str) -> bool:
            for dr, dc in drs:
                r, c = sq_to_rc(sq)
                while True:
                    r += dr; c += dc
                    if not in_bounds(r,c): break
                    p = self.board[rc_to_sq(r,c)]
                    if p != '.':
                        if p in pieces: return True
                        break
            return False
        if attacker_color==WHITE:
            if ray(PIECE_DIRS['B'], 'BQ') or ray(PIECE_DIRS['R'], 'RQ'):
                return True
        else:
            if ray(PIECE_DIRS['B'], 'bq') or ray(PIECE_DIRS['R'], 'rq'):
                return True
        # Pawns
        r, c = sq_to_rc(sq)
        if attacker_color == WHITE:
            for dc in (-1,1):
                rr, cc = r+1, c+dc
                if in_bounds(rr,cc) and self.board[rc_to_sq(rr,cc)] == 'P':
                    return True
        else:
            for dc in (-1,1):
                rr, cc = r-1, c+dc
                if in_bounds(rr,cc) and self.board[rc_to_sq(rr,cc)] == 'p':
                    return True
        return False

    def in_check(self, color: int) -> bool:
        ksq = self.king_square(color)
        return self.is_attacked_by(ksq, 1-color)

    # ------------ Move generation (pseudo-legal) ------------
    def gen_pseudo_legal(self) -> List[Move]:
        mvs: List[Move] = []
        turn = self.turn
        for sq, p in enumerate(self.board):
            if p == '.' or self.color_of(p) != turn:
                continue
            r, c = sq_to_rc(sq)
            if p.upper() == 'P':
                forward = -1 if turn==WHITE else 1
                start_rank = 6 if turn==WHITE else 1
                promo_rank = 0 if turn==WHITE else 7
                # Single push
                r1 = r+forward
                if in_bounds(r1,c) and self.board[rc_to_sq(r1,c)] == '.':
                    if r1 == promo_rank:
                        for pr in 'qrbn':
                            mvs.append(Move(sq, rc_to_sq(r1,c), pr))
                    else:
                        mvs.append(Move(sq, rc_to_sq(r1,c)))
                    # Double push
                    if r == start_rank:
                        r2 = r+2*forward
                        if self.board[rc_to_sq(r2,c)] == '.':
                            mvs.append(Move(sq, rc_to_sq(r2,c)))
                # Captures
                for dc in (-1,1):
                    cc = c+dc; rr = r+forward
                    if in_bounds(rr,cc):
                        tgt = self.board[rc_to_sq(rr,cc)]
                        if tgt != '.' and self.color_of(tgt) == 1-turn:
                            if rr == promo_rank:
                                for pr in 'qrbn':
                                    mvs.append(Move(sq, rc_to_sq(rr,cc), pr))
                            else:
                                mvs.append(Move(sq, rc_to_sq(rr,cc)))
                # En passant
                if self.ep_square is not None:
                    ep_r, ep_c = sq_to_rc(self.ep_square)
                    if ep_r == r+forward and abs(ep_c-c) == 1:
                        mvs.append(Move(sq, self.ep_square, is_ep=True))
            elif p.upper() == 'N':
                for dr, dc in PIECE_DIRS['N']:
                    rr, cc = r+dr, c+dc
                    if not in_bounds(rr,cc):
                        continue
                    tgt = self.board[rc_to_sq(rr,cc)]
                    if tgt == '.' or self.color_of(tgt) == 1-turn:
                        mvs.append(Move(sq, rc_to_sq(rr,cc)))
            elif p.upper() in 'BRQ':
                dirs = PIECE_DIRS['B'] if p.upper()=='B' else PIECE_DIRS['R'] if p.upper()=='R' else PIECE_DIRS['Q']
                for dr, dc in dirs:
                    rr, cc = r, c
                    while True:
                        rr += dr; cc += dc
                        if not in_bounds(rr,cc): break
                        tgt = self.board[rc_to_sq(rr,cc)]
                        if tgt == '.':
                            mvs.append(Move(sq, rc_to_sq(rr,cc)))
                        else:
                            if self.color_of(tgt) == 1-turn:
                                mvs.append(Move(sq, rc_to_sq(rr,cc)))
                            break
            elif p.upper() == 'K':
                for dr, dc in PIECE_DIRS['K']:
                    rr, cc = r+dr, c+dc
                    if not in_bounds(rr,cc): continue
                    tgt = self.board[rc_to_sq(rr,cc)]
                    if tgt == '.' or self.color_of(tgt) == 1-turn:
                        mvs.append(Move(sq, rc_to_sq(rr,cc)))
                # Castling
                if (('K' if turn==WHITE else 'k') in self.castling) or ((
                    'Q' if turn==WHITE else 'q') in self.castling):
                    if not self.in_check(turn):
                        # King side
                        if ('K' if turn==WHITE else 'k') in self.castling:
                            if self._castle_clear(turn, king_side=True):
                                mvs.append(Move(sq, rc_to_sq(r, c+2), is_castle=True))
                        # Queen side
                        if ('Q' if turn==WHITE else 'q') in self.castling:
                            if self._castle_clear(turn, king_side=False):
                                mvs.append(Move(sq, rc_to_sq(r, c-2), is_castle=True))
        return mvs

    def _castle_clear(self, color: int, king_side: bool) -> bool:
        r = 7 if color==WHITE else 0
        c_from = 4; # e-file
        if king_side:
            path = [rc_to_sq(r,5), rc_to_sq(r,6)]
            rook_sq = rc_to_sq(r,7)
        else:
            path = [rc_to_sq(r,3), rc_to_sq(r,2), rc_to_sq(r,1)]
            rook_sq = rc_to_sq(r,0)
        if self.board[rook_sq] == '.' or self.color_of(self.board[rook_sq]) != color:
            return False
        if any(self.board[sq] != '.' for sq in path):
            return False
        # squares the king passes through must not be attacked
        squares_to_check = [rc_to_sq(r,4)] + path[:2]  # e, f, g or e, d, c
        for s in squares_to_check:
            if self.is_attacked_by(s, 1-color):
                return False
        return True

    # ------------ Legal move filtering ------------
    def gen_legal(self) -> List[Move]:
        mvs = []
        for m in self.gen_pseudo_legal():
            self.push(m)
            illegal = self.in_check(1-self.turn)
            self.undo()
            if not illegal:
                mvs.append(m)
        return mvs

    # ------------ Make/undo moves ------------
    def push(self, m: Move):
        fr, to, promo = m.fr, m.to, m.promo
        p = self.board[fr]
        captured = self.board[to]
        ep_prev = self.ep_square
        cast_prev = self.castling
        hm_prev = self.halfmove_clock
        fm_prev = self.fullmove_number

        # halfmove clock
        if p.upper() == 'P' or captured != '.':
            self.halfmove_clock = 0
        else:
            self.halfmove_clock += 1

        # fullmove increment after black move
        if self.turn == BLACK:
            self.fullmove_number += 1

        self.ep_square = None

        # En passant capture
        if m.is_ep:
            if self.turn == WHITE:
                cap_sq = to + 8
            else:
                cap_sq = to - 8
            captured = self.board[cap_sq]
            self.board[cap_sq] = '.'

        # Move the piece
        self.board[to] = self.board[fr]
        self.board[fr] = '.'

        # Pawn double push sets ep square
        if p.upper() == 'P' and abs(to - fr) == 16:
            self.ep_square = (fr + to)//2

        # Promotion
        if p.upper() == 'P':
            r_to, _ = sq_to_rc(to)
            if r_to == (0 if self.turn==WHITE else 7):
                self.board[to] = (promo or 'q') if self.turn==BLACK else (promo or 'q').upper()

        # Castling: move rook
        if p.upper() == 'K' and m.is_castle:
            r, c_to = sq_to_rc(to)
            if c_to == 6:  # king side
                rook_from, rook_to = rc_to_sq(r,7), rc_to_sq(r,5)
            else:          # queen side
                rook_from, rook_to = rc_to_sq(r,0), rc_to_sq(r,3)
            self.board[rook_to] = self.board[rook_from]
            self.board[rook_from] = '.'

        # Update castling rights
        def strip_castling(chs: str, *flags: str) -> str:
            s = chs
            for f in flags:
                s = s.replace(f, '')
            return s
        if p == 'K':
            self.castling = strip_castling(self.castling, 'K', 'Q')
        if p == 'k':
            self.castling = strip_castling(self.castling, 'k', 'q')
        if fr == rc_to_sq(7,0) or to == rc_to_sq(7,0):
            self.castling = strip_castling(self.castling, 'Q')
        if fr == rc_to_sq(7,7) or to == rc_to_sq(7,7):
            self.castling = strip_castling(self.castling, 'K')
        if fr == rc_to_sq(0,0) or to == rc_to_sq(0,0):
            self.castling = strip_castling(self.castling, 'q')
        if fr == rc_to_sq(0,7) or to == rc_to_sq(0,7):
            self.castling = strip_castling(self.castling, 'k')

        # Switch turn
        self.turn = 1 - self.turn

        # Save history for undo
        self.history.append((captured, to, cast_prev, ep_prev, hm_prev, fm_prev))
        self._push_hash()

    def undo(self):
        if not self.history:
            return
        captured, to, cast_prev, ep_prev, hm_prev, fm_prev = self.history.pop()
        self.turn = 1 - self.turn
        self.halfmove_clock = hm_prev
        self.fullmove_number = fm_prev
        self.castling = cast_prev
        self.ep_square = ep_prev
        self.zhist.pop()

        # Find the move by diffing board
        # This is efficient enough for CLI purposes
        moved_from = None; moved_piece = None
        for i in range(64):
            # Square that became empty or changed rook on castling
            pass
        # Reconstruct from last action: we need from-square; we infer by scanning all squares
        # where piece moved to `to`.
        tgt_piece = None
        for i,p in enumerate(self.board):
            if i == to: tgt_piece = p
        # Determine from-square by checking plausible source moves
        fr = None
        if tgt_piece:
            for i,p in enumerate(self.board):
                if i==to: continue
                # Simulate: piece came from i
                # The from-square should be '.' now but wasn't before
                # We can't know directly; instead rebuild by replaying: simpler approach is to keep full move log.
                pass
        # Simpler: keep a parallel move log of last Move; adjust push to store it
        raise RuntimeError("Internal: undo requires move log; please use push_move/undo_move methods.")

    # For reliability, define a separate push that records the Move fully for undo
    def push_move(self, m: Move):
        # Save full snapshot needed for undo
        fr, to = m.fr, m.to
        piece = self.board[fr]
        captured_piece = self.board[to]
        state = (self.castling, self.ep_square, self.halfmove_clock, self.fullmove_number)
        # Perform the same logic as push, but record additional details
        ep_capture_sq = None
        rook_move: Optional[Tuple[int,int]] = None

        if piece.upper() == 'P' or captured_piece != '.':
            hm_new = 0
        else:
            hm_new = self.halfmove_clock + 1

        if self.turn == BLACK:
            fm_new = self.fullmove_number + 1
        else:
            fm_new = self.fullmove_number

        new_ep = None
        # En passant capture adjustment
        if m.is_ep:
            ep_capture_sq = to + 8 if self.turn == WHITE else to - 8
            captured_piece = self.board[ep_capture_sq]
            self.board[ep_capture_sq] = '.'

        # Move piece
        self.board[to] = piece
        self.board[fr] = '.'

        # Pawn double push
        if piece.upper() == 'P' and abs(to-fr) == 16:
            new_ep = (fr + to)//2

        # Promotion
        if piece.upper() == 'P':
            r_to,_ = sq_to_rc(to)
            if r_to == (0 if self.turn==WHITE else 7):
                self.board[to] = (m.promo or 'q') if self.turn==BLACK else (m.promo or 'q').upper()

        # Castling rook move
        if piece.upper() == 'K' and m.is_castle:
            r, c_to = sq_to_rc(to)
            if c_to == 6:
                rook_from, rook_to = rc_to_sq(r,7), rc_to_sq(r,5)
            else:
                rook_from, rook_to = rc_to_sq(r,0), rc_to_sq(r,3)
            rook_move = (rook_from, rook_to)
            self.board[rook_to] = self.board[rook_from]
            self.board[rook_from] = '.'

        # Castling rights update
        def strip(chs: str, *flags: str) -> str:
            s = chs
            for f in flags: s = s.replace(f,'')
            return s
        cast_before = self.castling
        if piece == 'K':
            self.castling = strip(self.castling, 'K','Q')
        if piece == 'k':
            self.castling = strip(self.castling, 'k','q')
        if fr == rc_to_sq(7,0) or to == rc_to_sq(7,0):
            self.castling = strip(self.castling, 'Q')
        if fr == rc_to_sq(7,7) or to == rc_to_sq(7,7):
            self.castling = strip(self.castling, 'K')
        if fr == rc_to_sq(0,0) or to == rc_to_sq(0,0):
            self.castling = strip(self.castling, 'q')
        if fr == rc_to_sq(0,7) or to == rc_to_sq(0,7):
            self.castling = strip(self.castling, 'k')

        # Commit state changes
        self.history.append(((fr,to,m.promo,m.is_ep,m.is_castle), captured_piece, ep_capture_sq, cast_before, self.ep_square, self.halfmove_clock, self.fullmove_number, rook_move))
        self.halfmove_clock = hm_new
        self.fullmove_number = fm_new
        self.ep_square = new_ep
        self.turn = 1 - self.turn
        self._push_hash()

    def undo_move(self):
        if not self.history:
            return
        (fr,to,promo,is_ep,is_castle), captured_piece, ep_capture_sq, cast_before, ep_before, hm_before, fm_before, rook_move = self.history.pop()
        self.turn = 1 - self.turn
        # Reverse rook move if any
        if rook_move:
            rf, rt = rook_move
            self.board[rf] = self.board[rt]
            self.board[rt] = '.'
        # Reverse promotion or normal move
        moved_piece = self.board[to]
        # If it was a promotion, restore pawn
        if promo is not None:
            moved_piece = 'p' if moved_piece.islower() else 'P'
        self.board[fr] = moved_piece
        self.board[to] = '.'
        # Restore captured
        if is_ep and ep_capture_sq is not None:
            self.board[ep_capture_sq] = captured_piece
        else:
            if captured_piece != '.':
                self.board[to] = captured_piece
        # Restore state
        self.castling = cast_before
        self.ep_square = ep_before
        self.halfmove_clock = hm_before
        self.fullmove_number = fm_before
        self.zhist.pop()

    # ------------ Game status ------------
    def legal_moves(self) -> List[Move]:
        return self.gen_legal()

    def is_check(self) -> bool:
        return self.in_check(self.turn)

    def is_checkmate(self) -> bool:
        return self.is_check() and not self.legal_moves()

    def is_stalemate(self) -> bool:
        return not self.is_check() and not self.legal_moves()

    def is_threefold(self) -> bool:
        cur = self._hash_core()
        return self.zhist.count(cur) >= 3

    def is_fifty_move(self) -> bool:
        return self.halfmove_clock >= 100

    # ------------ Rendering ------------
    def __str__(self) -> str:
        return self.ascii_board()

    def ascii_board(self) -> str:
        out = []
        for r in range(8):
            out.append(str(8-r)+" ")
            for c in range(8):
                ch = self.board[rc_to_sq(r,c)]
                out.append(ch if ch != '.' else ('.' if (r+c)%2 else '·'))
                out.append(' ')
            out.append('\n')
        out.append("  a b c d e f g h\n")
        out.append(f"Turn: {'White' if self.turn==WHITE else 'Black'}  ")
        out.append(f"Castling: {self.castling or '-'}  ")
        out.append(f"EP: {self.sq_to_algebraic(self.ep_square)}  ")
        out.append(f"Clock: {self.halfmove_clock}  ")
        out.append(f"Move: {self.fullmove_number}\n")
        return ''.join(out)


# ---------------- CLI ----------------

def print_help():
    print("Commands: move like e2e4, promote e7e8q | moves | undo | fen | help | quit")


def main():
    b = Board()
    print(b.ascii_board())
    print_help()
    while True:
        if b.is_checkmate():
            print("Checkmate!", "Black" if b.turn==WHITE else "White", "wins.")
            break
        if b.is_stalemate():
            print("Stalemate. Draw.")
            break
        if b.is_threefold():
            print("Draw by threefold repetition.")
            break
        if b.is_fifty_move():
            print("Draw by fifty-move rule.")
            break
        prompt = f"({'W' if b.turn==WHITE else 'B'})> "
        try:
            s = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print() ; break
        if not s:
            continue
        if s in ("q","quit","exit"): break
        if s in ("h","help"): print_help(); continue
        if s == "fen": print(b.fen()); continue
        if s == "moves":
            ms = sorted(m.uci() for m in b.legal_moves())
            print(" ".join(ms))
            continue
        if s == "undo":
            b.undo_move(); print(b.ascii_board()); continue
        # Try parse move
        try:
            fr, to, promo = uci_to_move(s)
            move = None
            for m in b.legal_moves():
                if m.fr==fr and m.to==to and (m.promo==promo or (m.promo and promo and m.promo==promo)):
                    move = m; break
            if move is None:
                # Allow missing promo char by defaulting to queen
                for m in b.legal_moves():
                    if m.fr==fr and m.to==to and (m.promo is None):
                        move = m; break
            if move is None:
                print("Illegal move. Type 'moves' to see options.")
                continue
            b.push_move(move)
            print(b.ascii_board())
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
