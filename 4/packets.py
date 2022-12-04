from util.constant_set import ConstantSet
from node import Node

class STATE_SYM(ConstantSet):
    READY = "p"
    DEFECT = "d"
    SENT = "-"

class State(Node):
    """
    A representation of a single board state.
    MCTS works by constructing a tree of these Nodes.
    Could be e.g. a chess or checkers board state.
    """
    def __init__(self, str):
        self.state = str

    def find_children(self):
        "All possible successors of this board state"
        
        return set()

    def find_random_child(self):
        "Random successor of this board state (for more efficient simulation)"
        return None

    def is_terminal(self):
        "Returns True if the node has no children"
        for i in range(len(self.state)):
            if self.state[i] == STATE_SYM.READY:
                return False
        return True

    def reward(self):
        "Assumes `self` is terminal node. 1=win, 0=loss, .5=tie, etc"
        for i in range(len(self.state)):
            if self.state[i] != STATE_SYM.SENT:
                return False
        return True

    def __hash__(self):
        "Nodes must be hashable"
        return 123456789

    def __eq__(node1, node2):
        "Nodes must be comparable"
        return True




    
