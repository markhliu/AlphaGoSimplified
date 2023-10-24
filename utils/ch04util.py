from copy import deepcopy
from random import choice

def MiniMax(env):
    # create a list to store winning moves
    wins=[]
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move and see what happens
        env_copy=deepcopy(env)
        new_state, reward, done, info = env_copy.step(m) 
        # if move m lead to a win now, take it
        if done and reward==1:
            return m 
        # see what's the best response from the opponent
        opponent_payoff=maximized_payoff(env_copy,reward,done)  
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        if my_payoff==1:
            wins.append(m)
    # pick winning moves if there is any        
    if len(wins)>0:
        return choice(wins)
    # otherwise randomly pick
    return env.sample()



def maximized_payoff(env, reward, done):
    # if the game has ended after the previous player's move
    if done:
        return -1
    # otherwise, search for action to maximize payoff
    best_payoff=-2
    # iterate through all possible next moves
    for m in env.validinputs:
        env_copy=deepcopy(env)
        new_state,reward,done,info=env_copy.step(m)  
        # what's the opponent's response
        opponent_payoff=maximized_payoff(env_copy, reward, done)
        # opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        # update your best payoff 
        if my_payoff>best_payoff:        
            best_payoff=my_payoff
    return best_payoff










