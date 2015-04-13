import bot_core

def think(state, quip):
  theMove = bot_core.UCT(state, 9999999, 1, verbose = True)
  print("UCTBot")
  return theMove
