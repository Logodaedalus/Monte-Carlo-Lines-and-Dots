import bot_core

def think(state, quip):
  theMove = bot_core.UCT(state, 5, 1, verbose = True)
  print("Move: ", theMove)
  return theMove
