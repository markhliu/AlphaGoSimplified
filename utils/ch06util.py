from copy import deepcopy
from random import choice

def maximized_payoff_ttt(env,reward,done,alpha,beta):
    # if the game has ended after the previous player's move
    if done:
        # if it's not a tie
        if reward!=0:
            return -1
        else:
            return 0
    if alpha==None:
        alpha=-2
    if beta==None:
        beta=-2
    if env.turn=="X":
        best_payoff = alpha
    if env.turn=="O":
        best_payoff = beta         
    # iterate through all possible moves
    for m in env.validinputs:
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m)  
        # If I make this move, what's the opponent's response?
        opponent_payoff=maximized_payoff_ttt(env_copy,\
                                     reward,done,alpha,beta)
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        if my_payoff > best_payoff:        
            best_payoff = my_payoff
            if env.turn=="X":
                alpha=best_payoff
            if env.turn=="O":
                beta=best_payoff 
        # skip the rest of the branch        
        if alpha>=-beta:
            break        
    return best_payoff        


def minimax_ttt(env):
    wins=[]
    ties=[]
    losses=[]  
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move and see what happens
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m) 
        # If player X wins right away with move m, take it.
        if done and reward!=0:
            return m 
        # See what's the best response from the opponent
        opponent_payoff=maximized_payoff_ttt(env_copy,\
                                     reward,done,-2,-2)  
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
    return choice(losses)      


def max_payoff_conn(env,reward,done,depth,alpha,beta):
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
    if alpha==None:
        alpha=-2
    if beta==None:
        beta=-2
    if env.turn=="red":
        best_payoff = alpha
    if env.turn=="yellow":
        best_payoff = beta         
    # iterate through all possible moves
    for m in env.validinputs:
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m)  
        # If I make this move, what's the opponent's response?
        opponent_payoff=max_payoff_conn(env_copy,\
                                reward,done,depth-1,alpha,beta)
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        if my_payoff > best_payoff:        
            best_payoff = my_payoff
            if env.turn=="red":
                alpha=best_payoff
            if env.turn=="yellow":
                beta=best_payoff   
        # Skip the rest of the branch
        if alpha>=-beta:
            break        
    return best_payoff        

def minimax_conn(env,depth=3):
    wins=[]
    ties=[]
    losses=[]  
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move and see what happens
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m) 
        # If player X wins right away with move m, take it.
        if done and reward!=0:
            return m 
        # See what's the best response from the opponent
        opponent_payoff=max_payoff_conn(env_copy,\
                            reward,done,depth,-2,-2)  
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
    return choice(losses)      









