def think(state, quip):
   bestScore = state.get_score()
   moves = state.get_moves()
   for move in moves:
      attempt = state.copy().apply_move(move)
      if attempt.get_score() > bestScore:
         bestMove = move
         bestScore = attempt.get_score()
   return bestMove
