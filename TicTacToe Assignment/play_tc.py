from TCGame_Env1 import TicTacToe
import random
import numpy as np
import pickle


class PlayTicTacToe():

  def __init__(self):
    self.env = TicTacToe()
    self.state = self.env.state

    with open('Policy.pkl', "rb") as policy_file:
      self.policy = pickle.load(policy_file)

  
  def Q_state(self, state):
    return ('-'.join(str(e) for e in state)).replace('nan','x')

  def random_action(self):
    agent_action_space = list(self.env.action_space(self.state)[0])
    return agent_action_space[np.random.choice(len(agent_action_space))]

  def get_agent_action(self):
    q_state = self.Q_state(self.state)
    if q_state in self.policy.keys():
      # pick best action per policy
      allowed_agent_actions = list(self.env.action_space(self.state)[0])
      allowed_actions = {key:self.policy[q_state][key] for key in self.policy[q_state].keys() if key in allowed_agent_actions}
      action = max(allowed_actions, key=allowed_actions.get)
    else:
      action = self.random_action()

    return action

  def start(self):    
    first_action = self.random_action()

    self.state, reward, is_terminal = self.env.step(self.state, first_action, True)

    self.print_state(self.state)

    while not is_terminal:
      agent_action = self.get_agent_action()

      self.state, reward, is_terminal = self.env.step(self.state, agent_action, True)

      self.print_state(self.state)

    if reward == 10:
      print('You Lose')
    elif reward == -10:
      print('You Win')
    else:
      print('Tie')

  def print_state(self, state, episode = '', time_step = '', reward = '', is_terminal=''):
    temp_state = state.copy()
    # temp_state[np.isnan(temp_state)] = 0
    temp_state = np.nan_to_num(temp_state, nan=0)
    print(temp_state[:3])
    print(temp_state[3:6])
    print(temp_state[6:])

if __name__ == '__main__':
  playTicTacToe = PlayTicTacToe()
  playTicTacToe.start()
