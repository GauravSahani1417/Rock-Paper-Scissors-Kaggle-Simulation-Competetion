
from random import randint
action = 0

def get_outcome(action, opponent_action):
    """ Return the outcome of the previous game """
    if action == ((opponent_action + 1) % 3):
        outcome = 1     # win
    elif opponent_action == ((action + 1) % 3):
        outcome = -1    # lose
    else:
        outcome = 0     # draw
    return outcome

def beat_a_human_agent(observation, configuration):
    """ Return an action: 0 - Rock, 1 - Paper, 2 - Scissors """
    global action    
    if observation.step == 0:
        action = randint(0, 2)
    else:
        previous_outcome = get_outcome(action, observation.lastOpponentAction)
        if previous_outcome == -1:
            action = list({0,1,2} - {action, observation.lastOpponentAction})[0]
        elif previous_outcome == 1:
            action = observation.lastOpponentAction
        else:
            action = randint(0, 2)
    return action
