
from copy import deepcopy
import numpy as np
from tensorflow import keras
from math import sqrt, log, inf

def select(priors,env,results,weight):    
    # weighted average of priors and rollout_value
    scores={}
    for k,v in results.items():
        # rollout_value for each next move
        if len(v)==0:
            vi=0
        else:
            vi=sum(v)/len(v);
        # scale the prior by (1+N(L))
        prior=priors[0][k-1]/(1+len(v))
        # calculate weighted average
        scores[k]=weight*prior+(1-weight)*vi
    # select child node based on the weighted average     
    return max(scores,key=scores.get) 

# expand game tree by selecting child node
def expand(env,move):
    env_copy=deepcopy(env)
    state,reward,done,info=env_copy.step(move)
    return env_copy, done, reward

# roll out a game till terminal state or depth reached
def simulate(env_copy,done,reward):
    # if the game has already ended
    if done==True:
        return reward
    # select moves based on fast policy network
    while True:
        move=env_copy.sample()
        state,reward,done,info=env_copy.step(move)
        # if terminal state is reached, returns outcome
        if done==True:
            return reward

def backpropagate(env,move,reward,results):
    # update results
    if env.turn=="X" or env.turn=="red":
        results[move].append(reward)
    # if current player is player 2,
    # multiply outcome with -1
    if env.turn=="O" or env.turn=="yellow":
        results[move].append(-reward)                  
    return results

def alphazero(env,weight,PG_net,num_rollouts=100):
    # if there is only one valid move left, take it
    if len(env.validinputs)==1:
        return env.validinputs[0]
    # get the prior from the PG policy network
    if env.turn=="X" or env.turn=="O":
        state = env.state.reshape(-1,9)
        conv_state = state.reshape(-1,3,3,1)
        if env.turn=="X":
            priors = PG_net([state,conv_state])
        elif env.turn=="O":
            priors = PG_net([-state,-conv_state])  
    if env.turn=="red" or env.turn=="yellow":
        state = env.state.reshape(-1,42)
        conv_state = state.reshape(-1,7,6,1)
        if env.turn=="red":
            priors = PG_net([state,conv_state])
        elif env.turn=="yellow":
            priors = PG_net([-state,-conv_state])          
    # create a dictionary results
    results={}
    for move in env.validinputs:
        results[move]=[]
    # roll out games
    for _ in range(num_rollouts):
        # select
        move=select(priors,env,results,weight)
        # expand
        env_copy, done, reward=expand(env,move)
        # simulate
        reward=simulate(env_copy,done,reward)
        # backpropagate
        results=backpropagate(env,move,reward,results)
    # select the most visited child node
    visits={k:len(v) for k,v in results.items()}
    return max(visits,key=visits.get)










