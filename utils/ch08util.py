import random
from copy import deepcopy

def simulate_a_game(env,counts,wins,losses):
    env_copy=deepcopy(env)
    actions=[]
    # play a full game
    while True:
        #randomly select a next move
        move=random.choice(env_copy.validinputs)
        actions.append(deepcopy(move))
        state,reward,done,info=env_copy.step(move)
        if done:
            counts[actions[0]] += 1
            if (reward==1 and env.turn==1) or \
                (reward==-1 and env.turn==2):
                wins[actions[0]] += 1
            if (reward==-1 and env.turn==1) or \
                (reward==1 and env.turn==2):
                losses[actions[0]] += 1                
            break
    return counts, wins, losses


def best_move(counts,wins,losses):
    # See which action is most promising
    scores={}
    for k,v in counts.items():
        if v==0:
            scores[k]=0
        else:
            scores[k]=(wins.get(k,0)-losses.get(k,0))/v
    return max(scores,key=scores.get) 


def naive_mcts(env, num_rollouts=10000):
    if len(env.validinputs)==1:
        return env.validinputs[0]
    counts={}
    wins={}
    losses={}
    for move in env.validinputs:
        counts[move]=0
        wins[move]=0
        losses[move]=0
    # roll out games
    for _ in range(num_rollouts):
        counts,wins,losses=simulate_a_game(env,counts,\
                                           wins, losses)
    return best_move(counts,wins,losses) 




from math import sqrt, log

def select(env,counts,wins,losses,temperature):
    # calculate the uct score for all next moves
    scores={}
    # the ones not visited get the priority
    for k in env.validinputs:
        if counts[k]==0:
            return k
    # total number of simulations conducted
    N=sum([v for k,v in counts.items()])
    for k,v in counts.items():
        if v==0:
            scores[k]=0
        else:
            # vi for each next move
            vi=(wins.get(k,0)-losses.get(k,0))/v
            exploration=temperature*sqrt(log(N)/counts[k])
            scores[k]=vi+exploration
    # Select the next move with the highest UCT score
    return max(scores,key=scores.get)  



def expand(env,move):
    env_copy=deepcopy(env)
    state,reward,done,info=env_copy.step(move)
    return env_copy, done, reward



def simulate(env_copy,done,reward):
    # if the game has already ended
    if done==True:
        return reward
    while True:
        move=env_copy.sample()
        state,reward,done,info=env_copy.step(move)
        if done==True:
            return reward



def backpropagate(env,move,reward,counts,wins,losses):
    # add 1 to the total game counts
    counts[move]=counts.get(move,0)+1
    # if the current player wins
    if reward==1 and (env.turn==1 or \
        env.turn=="X" or env.turn=="red"):
        wins[move]=wins.get(move,0)+1
    if reward==-1 and (env.turn==2 or \
        env.turn=="O" or env.turn=="yellow"):
        wins[move]=wins.get(move,0)+1        
    if reward==-1 and (env.turn==1 or \
        env.turn=="X" or env.turn=="red"):
        losses[move]=losses.get(move,0)+1
    if reward==1 and (env.turn==2 or \
        env.turn=="O" or env.turn=="yellow"):
        losses[move]=losses.get(move,0)+1       
    return counts,wins,losses

def next_move(counts,wins,losses):
    # See which action is most promising
    scores={}
    for k,v in counts.items():
        if v==0:
            scores[k]=0
        else:
            scores[k]=(wins.get(k,0)-losses.get(k,0))/v
    return max(scores,key=scores.get)


def mcts(env,num_rollouts=100,temperature=1.4):
    # if there is only one valid move left, take it
    if len(env.validinputs)==1:
        return env.validinputs[0]
    # create three dictionaries counts, wins, losses
    counts={}
    wins={}
    losses={}
    for move in env.validinputs:
        counts[move]=0
        wins[move]=0
        losses[move]=0
    # roll out games
    for _ in range(num_rollouts):
        # selection
        move=select(env,counts,wins,losses,temperature)
        # expansion
        env_copy, done, reward=expand(env,move)
        # simulation
        reward=simulate(env_copy,done,reward)      
        # backpropagate
        counts,wins,losses=backpropagate(\
            env,move,reward,counts,wins,losses)
    # make the move
    return next_move(counts,wins,losses)





