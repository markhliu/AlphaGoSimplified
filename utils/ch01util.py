import random
from utils.coin_env import coin_game


def rule_based_AI(env):
    if env.state%3 != 0:
        move = env.state%3
    else:
        move = env.sample()
    return move


def random_player(env):
    move = env.sample()
    return move


# Define the one_coin_game() function
def one_coin_game(player1, player2):
    env = coin_game()
    env.reset()     
    while True:    
        action = player1(env)  
        new_state, reward, done, info = env.step(action)
        if done:
            break
        action = player2(env)  
        new_state, reward, done, info = env.step(action)
        if done:
            break            
    return reward 