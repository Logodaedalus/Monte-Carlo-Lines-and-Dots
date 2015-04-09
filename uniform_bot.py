import random

def think(state, quip):
    x = random.choice(state.get_moves())
    output = "I'm randomly choosing " + str(x)
    quip(output)
    return x