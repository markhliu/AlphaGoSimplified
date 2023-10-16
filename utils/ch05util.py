from copy import deepcopy
from random import choice


def MiniMax_X(env):
    wins=[]
    ties=[]
    losses=[]  
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move and see what happens
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m) 
        # If player X wins right away with move m, take it.
        if done and reward==1:
            return m 
        # See what's the best response from the opponent
        opponent_payoff=maximized_payoff(env_copy,reward,done)  
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        if my_payoff==1:
            wins.append(m)
        elif my_payoff==0:
            ties.append(m)
        else:
            losses.append(m)
    # pick winning moves if there is any        
    if len(wins)>0:
        return choice(wins)
    # otherwise pick tying moves
    elif len(ties)>0:
        return choice(ties)
    return env.sample()


def maximized_payoff(env,reward,done):
    # if the game has ended after the previous player's move
    if done:
        # if it's not a tie
        if reward!=0:
            return -1
        else:
            return 0
    # Otherwise, search for action to maximize payoff
    best_payoff=-2
    # iterate through all possible moves
    for m in env.validinputs:
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m)  
        # If I make this move, what's the opponent's response?
        opponent_payoff=maximized_payoff(env_copy,reward,done)
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        # update your best payoff 
        if my_payoff>best_payoff:        
            best_payoff=my_payoff
    return best_payoff

def MiniMax_O(env):
    wins=[]
    ties=[]
    losses=[]  
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move and see what happens
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m) 
        # If player O wins right away with move m, take it.
        if done and reward==-1:
            return m 
        # See what's the best response from the opponent
        opponent_payoff=maximized_payoff(env_copy,reward,done)  
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        if my_payoff==1:
            wins.append(m)
        elif my_payoff==0:
            ties.append(m)
        else:
            losses.append(m)
    # pick winning moves if there is any        
    if len(wins)>0:
        return choice(wins)
    # otherwise pick tying moves
    elif len(ties)>0:
        return choice(ties)
    return env.sample()      


def max_payoff(env,reward,done,depth):
    # if the game has ended after the previous player's move
    if done:
        # if it's not a tie
        if reward!=0:
            return -1
        else:
            return 0
    # If the maximum depth is reached, assume tie game
    if depth==0:
        return 0        
    # Otherwise, search for action to maximize payoff
    best_payoff=-2
    # iterate through all possible moves
    for m in env.validinputs:
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m)  
        # If I make this move, what's the opponent's response?
        opponent_payoff=max_payoff(env_copy,reward,done,depth-1)
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        # update your best payoff 
        if my_payoff>best_payoff:        
            best_payoff=my_payoff
    return best_payoff

def MiniMax_depth(env,depth=3):
    wins=[]
    ties=[]
    losses=[]  
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move and see what happens
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m) 
        if done and reward!=0:
            return m 
        # See what's the best response from the opponent
        opponent_payoff=max_payoff(env_copy,reward,done,depth)  
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        if my_payoff==1:
            wins.append(m)
        elif my_payoff==0:
            ties.append(m)
        else:
            losses.append(m)
    # pick winning moves if there is any        
    if len(wins)>0:
        return choice(wins)
    # otherwise pick tying moves
    elif len(ties)>0:
        return choice(ties)
    return env.sample()      

