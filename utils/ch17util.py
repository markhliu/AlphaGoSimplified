
from copy import deepcopy
import numpy as np




def best_move_fast_net(env, fast_net):
    # priors from the policy network
    if env.turn=="X":
        state = env.state.reshape(-1,3,3,1)
        action_probs=fast_net(state)
    elif env.turn=="O":
        state = env.state.reshape(-1,3,3,1)
        action_probs=fast_net(-state)
    elif env.turn=="red":
        state = env.state.reshape(-1,7,6,1)
        action_probs=fast_net(state)
    elif env.turn=="yellow":
        state = env.state.reshape(-1,7,6,1)
        action_probs=fast_net(-state)             
    ps=[]
    for a in sorted(env.validinputs):
        ps.append(np.squeeze(action_probs)[a-1])
    ps=np.array(ps)
    return np.random.choice(sorted(env.validinputs),
        p=ps/ps.sum())

 
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
def simulate(env_copy,done,reward,depth,value_net,
             fast_net, policy_rollout=True):
    # if the game has already ended
    if done==True:
        return reward
    # select moves based on fast policy network
    for _ in range(depth):
        if policy_rollout:
            try:
                move=best_move_fast_net(env_copy, fast_net)
            except:move=env_copy.sample()
        else:
            move=env_copy.sample()
        state,reward,done,info=env_copy.step(move)
        # if terminal state is reached, returns outcome
        if done==True:
            return reward
    # depth reached but game not over, evaluate
    if env_copy.turn=="X":
        state=state.reshape(-1,3,3,1)
        ps=value_net.predict(state,verbose=0)
        # reward is prob(X win) - prob(O win)
        reward=ps[0][1]-ps[0][2]        
    elif env_copy.turn=="O":
        state=state.reshape(-1,3,3,1)
        ps=value_net.predict(-state,verbose=0)
        # reward is prob(X win) - prob(O win)
        reward=ps[0][2]-ps[0][1]     
    elif env_copy.turn=="red":
        state=state.reshape(-1,7,6,1)
        ps=value_net.predict(state,verbose=0)
        # reward is prob(red win) - prob(yellow win)
        reward=ps[0][1]-ps[0][2]        
    elif env_copy.turn=="yellow":
        state=state.reshape(-1,7,6,1)
        ps=value_net.predict(-state,verbose=0)
        # reward is prob(red win) - prob(yellow win)
        reward=ps[0][2]-ps[0][1]           
    return reward

def backpropagate(env,move,reward,results):
    # update results
    if env.turn=="X" or env.turn=="red":
        results[move].append(reward)
    # if current player is player 2, multiply outcome with -1
    if env.turn=="O" or env.turn=="yellow":
        results[move].append(-reward)                  
    return results

def alphago(env,weight,depth,PG_net,value_net,
        fast_net, policy_rollout=True,num_rollouts=100):
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
        reward=simulate(env_copy,done,reward,depth,value_net,
                     fast_net, policy_rollout)
        # backpropagate
        results=backpropagate(env,move,reward,results)
    # select the most visited child node
    visits={k:len(v) for k,v in results.items()}
    return max(visits,key=visits.get)




