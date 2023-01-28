import random
from copy import deepcopy
from math import log, sqrt


def uct_select(env_copy,path,paths,temperature):
    # use uct to select move
    parent=[]
    pathvs=[]
    for v in env_copy.validinputs:
        pathv=path+str(v)
        pathvs.append(pathv)
        for p in paths:
            if p[0]==pathv:
                parent.append(p)
    # calculate uct score for each action
    uct={}
    for pathv in pathvs:
        history=[p for p in parent if p[0]==pathv]
        if len(history)==0:
            uct[pathv]=float("inf")
        else:
            uct[pathv]=sum([p[1] for p in history])/len(history)+\
                temperature*sqrt(log(len(parent))/len(history))    
    move=max(uct,key=uct.get)
    move=int(move[-1])
    return move


def uct_simulate_ttt(env,paths,counts,wins,losses,temperature):
    env_copy=deepcopy(env)
    actions=[]
    path=""
    while True:
        utc_move=uct_select(env_copy,path,paths,temperature)
        move=deepcopy(utc_move)
        actions.append(move)
        state,reward,done,info=env_copy.step(move)
        path += str(move)
        if done:
            result=0
            counts[actions[0]] += 1
            if (reward==1 and env.turn=="X") or \
                (reward==-1 and env.turn=="O"):
                result=1
                wins[actions[0]] += 1
            if (reward==-1 and env.turn=="X") or \
                (reward==1 and env.turn=="O"):
                result=-1
                losses[actions[0]] += 1                
            break
    return result,path,counts,wins,losses

def uct_mcts_ttt(env, num_rollouts=100,temperature=1.4):
    if len(env.validinputs)==1:
        return env.validinputs[0]
    counts={}
    wins={}
    losses={}
    for move in env.validinputs:
        counts[move]=0
        wins[move]=0
        losses[move]=0
    paths=[]    
    # roll out games
    for _ in range(num_rollouts):
        result,path,counts,wins,losses=uct_simulate_ttt(\
         env,paths,counts,wins,losses,temperature)      
        # backpropagate
        backpropagate(path,result,paths)
    # See which action is most promising
    best_next_move=best_move(counts,wins,losses) 
    return best_next_move



# backpropagate
def backpropagate(path,result,paths):
    while path != "":
        paths.append((path,result))
        path=path[:-1]





def best_move(counts,wins,losses):
    # See which action is most promising
    scores={}
    for k,v in counts.items():
        if v==0:
            scores[k]=0
        else:
            scores[k]=(wins.get(k,0)-losses.get(k,0))/v
    best_move=max(scores,key=scores.get)  
    return best_move






def uct_simulate_conn(env,paths,counts,wins,losses,temperature):
    env_copy=deepcopy(env)
    actions=[]
    path=""
    while True:
        utc_move=uct_select(env_copy,path,paths,temperature)
        move=deepcopy(utc_move)
        actions.append(move)
        state,reward,done,info=env_copy.step(move)
        path += str(move)
        if done:
            result=0
            counts[actions[0]] += 1
            if (reward==1 and env.turn=="red") or \
                (reward==-1 and env.turn=="yellow"):
                result=1
                wins[actions[0]] += 1
            if (reward==-1 and env.turn=="red") or \
                (reward==1 and env.turn=="yellow"):
                result=-1
                losses[actions[0]] += 1                
            break
    return result,path,counts,wins,losses

def uct_mcts_conn(env,num_rollouts=100,temperature=1.4):
    if len(env.validinputs)==1:
        return env.validinputs[0]
    counts={}
    wins={}
    losses={}
    for move in env.validinputs:
        counts[move]=0
        wins[move]=0
        losses[move]=0
    paths=[]    
    # roll out games
    for _ in range(num_rollouts):
        result,path,counts,wins,losses=uct_simulate_conn(\
         env,paths,counts,wins,losses,temperature)      
        # backpropagate
        backpropagate(path,result,paths)
    # See which action is most promising
    best_next_move=best_move(counts,wins,losses) 
    return best_next_move













