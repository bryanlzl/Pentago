# Pentago (Python)

A university project done as part of a programming module.
As an interest, I have modified it by creating an interface and will continue to improve the overall code structure.

In the pentago.py file, the core functions are:

1) check_turn - Check's the validity of the current turn [game must always start with player 1] -
Input board and turn, Output True/False

2) check_move - Check's the validity of the player's move [player is not allowed to put on occupied pieces of the board] -
Input board, row, col, Output True/False

3) rotation - Rotates one of four 3x3 quadrant of the board once, either clockwise of anti-clockwise -
Input board and rot, Output board

4) victory_board - Checks the board for consecutive 5-in-a-row pieces to determine a win, full board with no player winning (draw) and no win conditions - 
Input board, Output 0/1/2/3 (0 no win/draw, 1 p1 win, 2 p2 win, 3 draw)

5) apply_move - Applies the move of 
