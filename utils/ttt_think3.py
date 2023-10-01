
import random
from copy import deepcopy


# moves that leads to X winning now
def check_Xwin1(env): 
    for m in env.validinputs:
        env_copy=deepcopy(env)
        state, reward, done, info = env_copy.step(m) 
        # Winning move for X
        if done and reward==1:
            return m                  
    return None
# moves leading to O winning next
def check_Owin2(env):
    for m1 in env.validinputs:
        for m2 in env.validinputs:
            if m1!=m2:
                env_copy=deepcopy(env)
                s,r,done,_=env_copy.step(m1) 
                s,r,done,_=env_copy.step(m2)
                if done and r==-1:
                    return m2                  
    return None
# look 3 steps ahead
def X_think3(env):
    # If there is only one move left, take it
    if len(env.validinputs) == 1:
        return env.validinputs[0]
    # Otherwise, see if there is a winning move   
    winner=check_Xwin1(env)
    if winner is not None:
        return winner
    # Otherwise, see if there is a losing move   
    loser=check_Owin2(env)
    if loser is not None:
        return loser
    # If only two moves left, randomly choose
    if len(env.validinputs)<=2:
        return random.choice(env.validinputs)    
    # Otherwise, look ahead
    w3=[]
    for m1 in env.validinputs:
        for m2 in env.validinputs:
            for m3 in env.validinputs:
                if m1!=m2 and m1!=m3 and m2!=m3:
                    env_copy=deepcopy(env)
                    s,r,done,_=env_copy.step(m1) 
                    s,r,done,_=env_copy.step(m2)   
                    s,r,done,_=env_copy.step(m3)                    
                    if done and r==1:
                        w3.append(m1) 
    # Choose the most frequent winner
    if len(w3)>0:
        return max(set(w3),key=w3.count)                
    # Take random move otherwise
    return random.choice(env.validinputs)





def check_Owin1(env): 
    for m in env.validinputs:
        env_copy=deepcopy(env)
        state, reward, done, info = env_copy.step(m) 
        if done and reward==-1:
            return m                  
    return None
# moves leading to O winning next
def check_Xwin2(env):
    for m1 in env.validinputs:
        for m2 in env.validinputs:
            if m1!=m2:
                env_copy=deepcopy(env)
                s,r,done,_=env_copy.step(m1) 
                s,r,done,_=env_copy.step(m2)
                if done and r==1:
                    return m2                  
    return None
# look 3 steps ahead
def O_think3(env):
    if len(env.validinputs) == 1:
        return env.validinputs[0]
    winner=check_Owin1(env)
    if winner is not None:
        return winner
    # Otherwise, see if there is a losing move   
    loser=check_Xwin2(env)
    if loser is not None:
        return loser
    # If only two moves left, randomly choose
    if len(env.validinputs)<=2:
        return random.choice(env.validinputs)    
    # Otherwise, look ahead
    w3=[]
    for m1 in env.validinputs:
        for m2 in env.validinputs:
            for m3 in env.validinputs:
                if m1!=m2 and m1!=m3 and m2!=m3:
                    env_copy=deepcopy(env)
                    s,r,done,_=env_copy.step(m1) 
                    s,r,done,_=env_copy.step(m2)   
                    s,r,done,_=env_copy.step(m3)                    
                    if done and r==-1:
                        w3.append(m1) 
    # Choose the most frequent winner
    if len(w3)>0:
        return max(set(w3),key=w3.count)                
    # Take random move otherwise
    return random.choice(env.validinputs)








