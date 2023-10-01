from utils.ttt_env import ttt
from copy import deepcopy

def ttt_think1(env):
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move
        env_copy=deepcopy(env)
        state,reward,done,_=env_copy.step(m) 
        # if reward is 1 or -1, current player wins
        if done and abs(reward)==1:
            # take the winning move
            return m                  
    # otherwise, randomly select a move
    return env.sample()

def ttt_random(env):
    move = env.sample()
    return move

def ttt_manual(env):
    print(f"game state is \n{env.state.reshape(3,3)[::-1]}") 
    while True:
        move = input(f"Player {env.turn}, what's your move?")
        try: 
            move = int(move)
        except:
            print("the move must be a number")
        if move in env.validinputs:
            return move
        else:
            print("please enter a valid move")

# Define the one_ttt_game() function
def one_ttt_game(player1, player2):
    env = ttt()
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


def ttt_think2(env):
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move
        env_copy=deepcopy(env)
        state,reward,done,_=env_copy.step(m) 
        # if reward is 1 or -1, current player wins
        if done and abs(reward)==1:
            # take the winning move
            return m  
    # otherwise, look two moves ahead
    for m1 in env.validinputs:
        for m2 in env.validinputs:
            if m1!=m2:
                env_copy=deepcopy(env)
                s,r,done,_=env_copy.step(m1) 
                s,r,done,_=env_copy.step(m2)                     
                # block opponent's winning move
                if done and r!=0:
                    return m2 
    # otherwise, return a random move               
    return env.sample()


def ttt_think3(env):
    # if there is only one move, don't search
    if len(env.validinputs)==1:
        return env.validinputs[0]
    # if middle cell is open, take it
    if 5 in env.validinputs:
        return 5
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move
        env_copy=deepcopy(env)
        state,reward,done,_=env_copy.step(m) 
        # if reward is 1 or -1, current player wins
        if done and abs(reward)==1:
            # take the winning move
            return m  
    # otherwise, look two moves ahead
    for m1 in env.validinputs:
        for m2 in env.validinputs:
            if m1!=m2:
                env_copy=deepcopy(env)
                s,r,done,_=env_copy.step(m1) 
                s,r,done,_=env_copy.step(m2)                     
                # block opponent's winning move
                if done and r!=0:
                    return m2 
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
        return max(w3,key=w3.count)                
    # Return random move otherwise
    return env.sample()
















