import time
import random
import math

class Node:
    def __init__(self, move = None, parent = None, state = None):
        self.move = move # the move that got us to this node - "None" for the root node
        self.parentNode = parent # "None" for the root node
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = state.get_moves() # future child nodes
        self.turn = state.get_whos_turn()
        
    def UCTSelectChild(self):
        """ Use the UCB1 formula to select a child node. Often a constant UCTK is applied so we have
            lambda c: c.wins/c.visits + UCTK * math.sqrt(2*math.log(self.visits)/c.visits to vary the amount of
            exploration versus exploitation.
            Has to be float(c.wins)/c.visits from Piazza clue
        """
        s = sorted(self.childNodes, key = lambda c: float(c.wins)/c.visits + math.sqrt(2*math.log(self.visits)/c.visits))[-1]
        return s
   
    def AddChild(self, m, s):
        #Remove m from untriedMoves and add a new child node for this move.
        #    Return the added child node       
        n = Node(move = m, parent = self, state = s)
        self.untriedMoves.remove(m)
        self.childNodes.append(n)
        return n
    
    def Update(self, result):
        # Update this node - one additional visit and result additional wins. result must be from the viewpoint of playerJustmoved.
        
        self.visits += 1
        self.wins += result

    def __repr__(self):
        return "[M:" + str(self.move) + " Wins/Visits:" + str(self.wins) + "/" + str(self.visits) + " U:" + str(self.untriedMoves) + "]"

    def TreeToString(self, indent):
        s = self.IndentString(indent) + str(self)
        for c in self.childNodes:
             s += c.TreeToString(indent+1)
        return s

    def IndentString(self,indent):
        s = "\n"
        for i in range (1,indent+1):
            s += "| "
        return s

    def ChildrenToString(self):
        s = ""
        for c in self.childNodes:
             s += str(c) + "\n"
        return s

def UCT(rootstate, iterdepth, itertime, verbose = False):

    rootnode = Node(state = rootstate)      #set the root to current root passed in
    timeout = time.time() + itertime        #set the timeout

    rps = 0

    while time.time() < timeout:
        currentDepth = 0
        node = rootnode
        state = rootstate.copy()
        # Select
        while node.untriedMoves == [] and node.childNodes != []: # node is fully expanded and non-terminal
            node = node.UCTSelectChild()
            state.apply_move(node.move)
        
        # Expand
        if node.untriedMoves != []: # if we can expand (i.e. state/node is non-terminal)
            m = random.choice(node.untriedMoves) 
            state.apply_move(m)
            node = node.AddChild(m,state) # add child and descend tree

        # Rollout - this can often be made orders of magnitude quicker using a state.GetRandomMove() function
        while state.get_moves() != [] and currentDepth <= iterdepth: # while state is non-terminal
            state.apply_move(random.choice(state.get_moves()))
            rps+=1
            currentDepth+=1
        
        # Backpropagate
        while node != None: # backpropagate from the expanded node and work back to the root node
            if (node.parentNode != None):
                node.Update(state.get_score()[node.parentNode.turn])
            else:
                node.Update(state.get_score()[node.turn])

            node = node.parentNode

    print "Rollouts per second: " + str(rps / itertime)
    return sorted(rootnode.childNodes, key = lambda c: c.visits)[-1].move # return the move that was most visited
