import bot_core

def think(state, quip):
    x = bot_core.UCT(rootstate = state, iterdepth = 5, itertime = 1, verbose = True)
    output = "I'm quickly choosing " + str(x)
    quip(output)
    return x
