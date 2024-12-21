# december_escapes.my_player.py
import math # we need it for diagonal movement logic, to offer sqrt(2)
# encapsulation, class definition
# functions inside class, method
class Player:
    """
    < FSM, finite state machine logic >
    freezed condition
        -1: freezed / none
    normal conditions 
        0: right
        1: up
        2: left
        3: down
    diagonal condition
        4: diagonal
    """
    def reset(self):
        print("you r reseting")
        self.velocity_x = 0
        self.velocity_y = 0
    def freeze(self):
        print("you r freezed")
        self.velocity_x = 0
        self.velocity_y = 0
    def checkDiagonal(self):
        if (
            abs(self.speed - math.hypot(self.velocity_x, self.velocity_y)) < 0.01 # you actually speed being reasonable
            or 
            (self.velocity_x == 0 and self.velocity_y == 0) # you are freezed
        ): return
        # you ARE in diagonal
        print("you r in diagonal")
        self.velocity_x = self.velocity_x / math.sqrt(2)
        self.velocity_y = self.velocity_y / math.sqrt(2)
        self.state = 4
    def get_state(self): ## Getter, (accessibility, everywhere both in mutable or immutable objects) 
        return self.state
    def get_position(self):
        return (self.x, self.y)
    def set_state(self, state): ## Setter, (mutable or immutable) 
        self.state = state
        self.reset() # for restting velocities
        if self.state == 0: self.velocity_x = self.speed
        if self.state == 1: self.velocity_y = -self.speed
        if self.state == 2: self.velocity_x = -self.speed
        if self.state == 3: self.velocity_y = self.speed
        if self.state == -1: self.freeze()
        if self.state == -1: self.freeze()
        self.checkDiagonal()
    def __init__(self, x, y, speed): ## constructor (__init__: the very first method being called only for initialization.)
        self.x = x
        self.y = y
        self.speed = speed
        self.velocity_x = 0
        self.velocity_y = 0
        self.state = 0
