#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW10 - Object Oriented Programming
"""

class Room: # entire class provided
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "Room(name: {})".format(self.name)

class Task:
    def __repr__(self): # provided
        return "Task(name: {}, isCompleted: {})".format(self.name, self.isCompleted)

    def __init__(self, name, isCompleted = False):
        self.name = name
        self.isCompleted = isCompleted

    def __eq__(self, other):
        return (self.name, self.isCompleted) == (other.name, other.isCompleted)

class Crewmate:
    def __init__(self, name, color, accessories = ()):
        # [your implementation]
        return

    def doTask(self, Task):
        # [your implementation]
        return None

    def vote(self, AmongUs):
        # [your implementation]
        # Default: vote for self if no candidate matches.
        return self

    def __repr__(self): # provided
        return "Crewmate(name: {}, color: {})".format(self.name, self.color)

    def callMeeting(self, AmongUs):
        # [your implementation]
        return
        

    def __eq__(self, other = False): # provided
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class Impostor:
    def __init__(self, name, color, accessories = ()):
        # [your implementation]
        return

    def eliminate(self, person):
        # [your implementation]
        return

    def vote(self, AmongUs):
        # [your implementation]
        # Default: vote for self if no candidate matches.
        return self

    def __repr__(self): # provided
        return "Impostor(name: {}, color: {})".format(self.name, self.color)

    def __str__(self):
        return "My name is {} and I'm an impostor.".format(self.name)

    def __eq__(self, other): # provided
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class AmongUs:
    def __init__(self, maxPlayers):
        # [your implementation]
        return

    def registerPlayer(self, person):
        # [your implementation]
        return None

    def registerTask(self, newTask, newRoom):
        # [your implementation]
        return None

    def gameOver(self):
        # [your implementation]
        return "Game is not over yet!"

    def __repr__(self): # provided
        return "AmongUs(maxPlayers: {})".format(self.maxPlayers)