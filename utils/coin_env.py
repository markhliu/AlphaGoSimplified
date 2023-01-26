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
        self.showboard=False   
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
        # Give the turn to the other player
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1             
        return self.state, self.reward, self.done, self.info

    def display_board(self):
        # Set up the screen
        try:
            t.setup(600,500,10,70) 
        except t.Terminator:
            t.setup(600,500,10,70)   
        t.tracer(False)
        t.hideturtle()
        t.bgcolor("lavender")
        t.title("Last Coin Standing")
        # Create a second turtle to show coins left
        self.left = t.Turtle()
        self.left.up()
        self.left.hideturtle()
        self.left.goto(-120,-200)
        self.left.write(f"Coins left:   {self.state}", font = ('Arial',30,'normal'))
        self.left.up()
        self.left.goto(-200,150)
        self.left.write(f"Player {self.turn}'s turn to move",font = ('Arial',30,'normal'))
        # Load a picture of the coin
        coin = PhotoImage(file = "files/ch01/cash.png").subsample(10,10)
        t.addshape("coin", t.Shape("image", coin))
        # Create 21 coin on screen 
        self.coins = [0]*21
        for i in range(21):
            self.coins[i] = t.Turtle('coin')
            self.coins[i].up()
            self.coins[i].goto(-150+50*(i//3),50-50*(i%3))
        t.update()

    def render(self):
        if self.showboard==False:
            self.display_board()
            self.showboard=True   
        # Update the number of coins left
        self.left.clear()
        self.left.goto(-120,-200)
        self.left.write(f"Coins left:   {self.state}", font = ('Arial',30,'normal'))
        self.left.goto(-200,150)
        self.left.write(f"Player {self.turn}'s turn to move",font = ('Arial',30,'normal'))

        # Remove a coin       
        if self.move==1:
            self.coins[self.state].hideturtle()              
        if self.move==2:
            self.coins[self.state+1].hideturtle()
            self.coins[self.state].hideturtle()                    
        t.update()                    


    def close(self):
        time.sleep(1)
        try:
            t.bye()
        except t.Terminator:
            print('exit turtle')
            
            
            
        