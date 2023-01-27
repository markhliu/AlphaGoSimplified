from random import choice
from copy import deepcopy


def minimax_X(env):
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
    return choice(losses)



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


def minimax_O(env):
    wins=[]
    ties=[]
    losses=[]  
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move and see what happens
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m) 
        # If player X wins right away with move m, take it.
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
    return choice(losses)      



def AI_think3(env):
    # See if there is a winning move 
    winner=AI_think1(env)
    # if yes, take it
    if winner is not None:
        return winner
    # check if opponent has a winning move
    loser=AI_think2(env)
    # if yes, block it
    if loser is not None:
        return loser
    # look three steps ahead
    w3=[]
    for m1 in env.validinputs:
        for m2 in env.validinputs:
            for m3 in env.validinputs:
                if m1!=m2 and m1!=m3 and m2!=m3:
                    env_copy=deepcopy(env)
                    s,r,done,_=env_copy.step(m1) 
                    s,r,done,_=env_copy.step(m2)   
                    s,r,done,_=env_copy.step(m3)                    
                    if done and r!=0:
                        w3.append(m1) 
    # Choose the most frequent winner
    if len(w3)>0:
        return max(set(w3),key=w3.count)                
    # Return None otherwise
    return None

def AI_think2(env):
    # See if there is a winning move 
    winner=AI_think1(env)
    # if yes, take it
    if winner is not None:
        return winner
    # otherwise, iterate through all possible next two moves
    for m1 in env.validinputs:
        for m2 in env.validinputs:
            if m1!=m2:
                env_copy=deepcopy(env)
                s,r,done,_=env_copy.step(m1) 
                s,r,done,_=env_copy.step(m2)                     
                # block your opponent's winning move
                if done and r!=0:
                    return m2 
    # otherwise, return None               
    return None

def AI_think1(env):
    # iterate through all possible next moves
    for m in env.validinputs:
        # make hypothetical moves
        env_copy=deepcopy(env)
        new_state, reward, done, info = env_copy.step(m) 
        # if the reward is 1 or -1, then the player wins
        if done and abs(reward)==1:
            return m                  
    return None

def test_ttt_game(env,player1,player2):  
    env.reset()   
    while True:       
        move=player1(env)
        if move==None:
            move=choice(env.validinputs)
        state,reward,done,_=env.step(move)
        if done:
            return reward            
        move=player2(env)
        if move==None:
            move=choice(env.validinputs)
        state,reward,done,_=env.step(move)
        if done:
            return reward 


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

def minimax(env,depth=3):
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
    return choice(losses)      







def conn_think1(env):
    for m in env.validinputs:
        env_copy=deepcopy(env)
        new_state, reward, done, info = env_copy.step(m) 
        if done and abs(reward)==1:
            return m                  
    return None

        
def test_conn_game(env,player1,player2): 
    #env=conn()
    env.reset()   
    while True:       
        move=player1(env)
        if move==None:
            move=choice(env.validinputs)
        state,reward,done,_=env.step(move)
        if done:
            return reward            
        move=player2(env)
        if move==None:
            move=choice(env.validinputs)
        state,reward,done,_=env.step(move)
        if done:
            return reward         
        
      
        
def to_avoid(env):
    toavoid=[]
    # look for ones you should avoid
    for m in env.validinputs:
        if len(env.occupied[m-1])<=4:
            env_copy=deepcopy(env)
            s,r,done,_=env_copy.step(m) 
            s,r,done,_=env_copy.step(m)                     
            if done and r==-1:
                toavoid.append(m) 
    return toavoid


def conn_think2(env):
    # See if there is a winning move 
    winner=conn_think1(env)
    # if yes, take it
    if winner is not None:
        return winner
    # look for ones you should block
    for m1 in env.validinputs:
        for m2 in env.validinputs:
            if m1!=m2:
                env_copy=deepcopy(env)
                s,r,done,_=env_copy.step(m1) 
                s,r,done,_=env_copy.step(m2)                     
                # block your opponent's winning move
                if done and r!=0:
                    return m2 
    # look for ones you should avoid
    toavoid=to_avoid(env)
    if len(toavoid)>0:
        leftovers=[i for i in env.validinputs if i not in toavoid]
        if len(leftovers)>0:
            return choice(leftovers)
    # return None otherwise
    return None       

def conn_think3(env):
    # See if there is value from AI_think2() 
    think2=AI_think2(env)
    # if yes, take it
    if think2 is not None:
        return think2
    # look 3 steps ahead
    w3=[]
    for m1 in env.validinputs:
        for m2 in env.validinputs:
            for m3 in env.validinputs:
                try:
                    env_copy=deepcopy(env)
                    s,r,done,_=env_copy.step(m1) 
                    s,r,done,_=env_copy.step(m2)   
                    s,r,done,_=env_copy.step(m3)                    
                    if done and r!=0:
                        w3.append(m1) 
                except:
                    pass
    # Choose the most frequent winner
    if len(w3)>0:
        return max(set(w3),key=w3.count)                
    # Take random move otherwise
    return choice(env.validinputs)








