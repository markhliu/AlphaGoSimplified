from random import choice
from copy import deepcopy


def position_eval(env,model):
    # obtain the current state, reshape it      
    state=env.state.reshape(-1,7,6,1)
    pred=model.predict(state,verbose=0)
    # prob(win)-prob(opponent wins)
    evaluation=pred[0][1]-pred[0][2]
    return evaluation 


def eval_payoff_conn(env,model,reward,done,depth,alpha,beta):
    # if the game has ended after the previous player's move
    if done:
        # if it's not a tie
        if reward!=0:
            return -1
        else:
            return 0
    # If the maximum depth is reached, assume tie game
    if depth==0:
        if env.turn=="red":
            return position_eval(env,model) 
        else:
            return -position_eval(env,model)    
    if alpha==None:
        alpha=-2
    if beta==None:
        beta=-2
    if env.turn=="red":
        best_payoff = alpha
    if env.turn=="yellow":
        best_payoff = beta         
    # iterate through all possible moves
    for m in env.validinputs:
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m)  
        # If I make this move, what's the opponent's response?
        opponent_payoff=eval_payoff_conn(env_copy,model,\
                             reward,done,depth-1,alpha,beta)
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        if my_payoff > best_payoff:        
            best_payoff = my_payoff
            if env.turn=="red":
                alpha=best_payoff
            if env.turn=="yellow":
                beta=best_payoff       
        if alpha>=-beta:
            break        
    return best_payoff 



def MiniMax_conn_eval(env,model,depth=3):
    values={} 
    # iterate through all possible next moves
    for m in env.validinputs:
        # make a hypothetical move and see what happens
        env_copy=deepcopy(env)
        state,reward,done,info=env_copy.step(m) 
        # If current player wins with m, take it.
        if done and reward!=0:
            return m 
        # See what's the best response from the opponent
        opponent_payoff=eval_payoff_conn(env_copy,\
                             model,reward,done,depth,-2,-2)  
        # Opponent's payoff is the opposite of your payoff
        my_payoff=-opponent_payoff 
        values[m]=my_payoff
    # pick the move with the highest value       
    best_move=max(values,key=values.get)
    return best_move 









