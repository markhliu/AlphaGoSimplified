
from copy import deepcopy
import numpy as np
from tensorflow import keras

# Load the trained actor critic model
model=keras.models.load_model("files/ac_coin.h5")

def onehot_encoder(state):
    onehot=np.zeros((1,22))
    onehot[0,state]=1
    return onehot

 
def select(priors,env,results,weight):    
    # weighted average of priors and rollout_value
    scores={}
    for k,v in results.items():
        # rollout_value for each next move
        if len(v)==0:
            vi=0
        else:
            vi=sum(v)/len(v)
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
def simulate(env_copy,done,reward,depth):
    # if the game has already ended
    if done==True:
        return reward
    for _ in range(depth):
        move=env_copy.sample()
        state,reward,done,info=env_copy.step(move)
        # if terminal state is reached, returns outcome
        if done==True:
            return reward
    # depth reached but game not over, evaluate
    onehot_state=onehot_encoder(state)
    # use the trained actor critic model to evaluate
    action_probs, critic_value = model(onehot_state)
    # output is predicted game outcome  
    return critic_value[0,0]

def backpropagate(env,move,reward,results):
    # if the current player is Player 1, update results
    if env.turn==1:
        results[move].append(reward)
    # if the current player is Player 2, multiply outcome with -1
    elif env.turn==2:
        results[move].append(-reward)                  
    return results

def alphazero_coin(env,weight,depth,num_rollouts=100):
    # if there is only one valid move left, take it
    if len(env.validinputs)==1:
        return env.validinputs[0]
    # get the prior from the AC policy network
    onehot_state = onehot_encoder(env.state)
    priors, _ = model(onehot_state)    
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
        reward=simulate(env_copy,done,reward,depth)
        # backpropagate
        results=backpropagate(env,move,reward,results)
    # select the most visited child node
    visits={k:len(v) for k,v in results.items()}
    return max(visits,key=visits.get)

