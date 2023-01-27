from copy import deepcopy
import random

def AI_think1(env):
    for m in env.validinputs:
        env_copy=deepcopy(env)
        new_state, reward, done, info = env_copy.step(m) 
        if done and abs(reward)==1:
            return m                  
    return None


def AI_vs_manual(env,player_function):
    manual=input("Do you want to be red or yellow?")
    if manual.lower()=="red":
        player="red"
    elif manual.lower()=="yellow":
        player="yellow"    
    state=env.reset()
    print(f"the current state is state=\n{state.T[::-1]}")
    # if you chose red, you move first
    if player=="red":
        move=input("enter your move:")
        state,reward,done,_=env.step(int(move))
        print(f"you have chosen move {move}")    
    while True:       
        # AI moves
        AI_move=player_function(env)
        if AI_move==None:
            AI_move=random.choice(env.validinputs)
        state,reward,done,_=env.step(AI_move)
        print(f"AI has chosen move {AI_move}")
        print(f"the current state is state=\n{state.T[::-1]}")
        if done and reward!=0:
            print("the AI player won")
            break
        if done and reward==0:
            print("game over; it's a tie") 
            break               
        move=input("enter your move:")
        state,reward,done,_=env.step(int(move))
        print(f"you have chosen move {move}")
        print(f"the current state is state=\n{state.T[::-1]}")         
        if done and reward!=0:
            print("the human player won")
            break
        if done and reward==0:
            print("game over; it's a tie")
            break  

def test_game(env,player1,player2):   
    env.reset()   
    while True:       
        move=player1(env)
        if move==None:
            move=random.choice(env.validinputs)
        state,reward,done,_=env.step(move)
        if done:
            return reward            
        move=player2(env)
        if move==None:
            move=random.choice(env.validinputs)
        state,reward,done,_=env.step(move)
        if done:
            return reward 


def random_player(env):               
    return random.choice(env.validinputs)


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
def AI_think2(env):
    # See if there is a winning move 
    winner=AI_think1(env)
    # if yes, take it
    if winner is not None:
        return winner
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
    # return None otherwise
    return None

def AI_think3(env):
    # See if there is value from AI_think2() 
    think2=AI_think2(env)
    # if yes, take it
    if think2 is not None:
        return think2
    # look 3 steps ahead
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
        return max(set(w3),key=w3.count)                
    # Take random move otherwise
    return random.choice(env.validinputs)