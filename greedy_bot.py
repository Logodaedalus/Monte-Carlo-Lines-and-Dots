import bot_core

def think(state, quip):
    #This should be UCT with a look depth of 1? 
    #UCT(rootstate, 1, itertime, verbose = False):
    x = bot_core.UCT(rootstate = state, iterdepth = 1, itertime = 1, verbose = True)
    output = "I'm greedily choosing " + bot_core.test("greedy")
    quip(output)
    return x
