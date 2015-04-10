import bot_core

def think(state, quip):
  return bot_core.UCT(state, 245, 1, verbose = True)
