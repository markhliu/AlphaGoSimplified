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
    best_move=max(scores,key=scores.get)  
    return best_move


def naive_mcts(env, num_rollouts=100):
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
    best_next_move=best_move(counts,wins,losses)  
    return best_next_move








