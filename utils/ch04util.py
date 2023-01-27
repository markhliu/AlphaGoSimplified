

from copy import deepcopy
from random import choice

def minimax(env):
    # create a list to store winning moves
    wins=[]
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move and see what happens
        env_copy=deepcopy(env)
        new_state, reward, done, info = env_copy.step(m) 
        # If wins right away with move m, take it.
        if done and reward==1:
            return m 
        # See what's the best response from the opponent
        opponent_payoff=maximized_payoff(env_copy, reward, done)  
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        if my_payoff==1:
            wins.append(m)
    # pick winning moves if there is any        
    if len(wins)>0:
        return choice(wins)
    # otherwise randomly pick
    return choice(env.validinputs)

def maximized_payoff(env, reward, done):
    # if the game has ended after the previous player's move
    if done:
        return -1
    # Otherwise, search for action to maximize payoff
    best_payoff=-2
    # iterate through all possible moves
    for m in env.validinputs:
        env_copy=deepcopy(env)
        new_state,reward,done,info=env_copy.step(m)  
        # If I make this move, what's the opponent's response
        opponent_payoff=maximized_payoff(env_copy, reward, done)
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        # update your best payoff 
        if my_payoff>best_payoff:        
            best_payoff=my_payoff
    return best_payoff



def rule_based_AI(env):
    state=int(env.state)
    if state%3 != 0:
        move = state%3
    else:
        move = choice([1,2])
    return move

def random_player(env):
    return choice(env.validinputs)

def test_coin_game(env,player1,player2):
    state=env.reset()   
    while True:
        action=player1(env)   
        state,reward,done,info=env.step(action)
        if done:
            return 1 
        action=player2(env)   
        state,reward,done,info=env.step(action)
        if done:
            return -1
