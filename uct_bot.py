import bot_core

def think(state, quip):
  theMove = bot_core.UCT(state, 999999999, 1, verbose = True)
  quip("I'm strategically choosing " + str(theMove))
  return theMove
