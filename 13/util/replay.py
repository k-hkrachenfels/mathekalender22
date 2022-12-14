from collections import namedtuple, deque
from typing import Type
import random

from collections import namedtuple

class ReplayMemory(object):
    
    def __init__(self, capacity, type: Type):
        self.type = type
        self.memory = deque([],maxlen=capacity)

    def push(self, *args):
        """Save a transition"""
        self.memory.append(self.type(*args))

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)

