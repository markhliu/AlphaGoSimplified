import turtle as t
from random import choice
from tkinter import messagebox
from tkinter import PhotoImage
import time
import numpy as np

# Define an action_space helper class
class action_space:
    def __init__(self, n):
        self.n = n
    def sample(self):
        num = np.random.choice(range(self.n))
        # covert to 1 to 9 in string format 
        action = str(1+num)
        return action
    
# Define an obervation_space helper class    
class observation_space:
    def __init__(self, n):
        self.shape = (n,)

class coin_game():
    def __init__(self): 
        # use the helper action_space class
        self.action_space=action_space(2)
        # use the helper observation_space class
        self.observation_space=observation_space(1)
        self.info=""   
        # set the game to the initial state
        self.reset()
    def reset(self):  
        # The player 1 moves first
        self.turn = 1
        # Count how many coins left
        self.state = 21
        # Create a list of valid moves
        self.validinputs = [1, 2] if self.state>2 else [1]
        # Whether the game is over
        self.done=False
        self.reward=0
        self.move=0
        return self.state               
    # step() function: make a move and update state
    def step(self, inp):
        # choice of the move must be 1 or 2
        assert int(inp)==1 or int(inp)==2
        if self.state==1:
            self.move=1
        else:
            self.move=int(inp)
        # update the state
        self.state -= self.move
        # check if the player has won the game
        if self.state == 0:
            self.done=True
            # reward is 1 if player 1 won; -1 otherwise
            self.reward=2*(self.turn==1)-1
        else:
            # Give the turn to the other player
            if self.turn == 1:
                self.turn = 2
            else:
                self.turn = 1             
        return self.state, self.reward, self.done, self.info
    
            
        