import random

def copy_opponent_agent(obs, config):
    if obs.step > 0:
        return obs.lastOpponentAction
    else:
        random.randint(0,2)
