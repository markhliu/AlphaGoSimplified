from utils.conn_env import conn
from copy import deepcopy
import random

def conn_think1(env):
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move
        env_copy=deepcopy(env)
        state,reward,done,_=env_copy.step(m) 
        # take the winning move
        if done and reward!=0:
            return m                  
    return env.sample()

def conn_random(env):
    move = env.sample()
    return move

def conn_manual(env):
    print(f"game state is \n{env.state.T[::-1]}") 
    while True:
        move=input(f"{env.turn} player, enter your move:")
        try: 
            move=int(move)
        except:
            print("the move must be a number")
        if move in env.validinputs:
            return move
        else:
            print("please enter a valid move")


# Define the one_conn_game() function
def one_conn_game(player1, player2):
    env = conn()
    env.reset()     
    while True:    
        action = player1(env)  
        state, reward, done, _ = env.step(action)
        if done:
            break
        action = player2(env)  
        state, reward, done, _ = env.step(action)
        if done:
            break            
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
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move
        env_copy=deepcopy(env)
        state,reward,done,_=env_copy.step(m) 
        # take the winning move
        if done and reward!=0:
            return m                  
    # otherwise, look two moves ahead
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
            return random.choice(leftovers)
    # otherwise, return a random move               
    return env.sample()










def conn_think3(env):
    # if there is only one valid move left
    if len(env.validinputs)==1:
        return env.validinputs[0]
    # take column 4 if it's empty
    if len(env.occupied[3])==0:
        return 4
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move
        env_copy=deepcopy(env)
        state,reward,done,_=env_copy.step(m) 
        # take the winning move
        if done and reward!=0:
            return m                  
    # otherwise, look two moves ahead
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
            return random.choice(leftovers)
    # look three steps ahead
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
        return max(w3,key=w3.count)                
    # otherwise, return a random move               
    return env.sample()













