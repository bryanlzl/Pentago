# Pentago (Python)

A university project done as part of a programming module.
As an interest, I have modified it by creating an interface and will continue to improve the overall code structure.

In the pentago.py file, the core functions are:

1) check_turn - Check's validity of the current turn [game must always start with player 1] -
Input board and turn, Output True/False

2) check_move - Check's validity of the player's move [player is not allowed to put on occupied pieces of the board] -
Input board, row, col, Output True/False

3) rotation - Rotates one of four 3x3 quadrant of the board once, either clockwise of anti-clockwise (refer to rotateIDpic) -
Input board and rot, Output board

4) victory_board - Checks board for consecutive 5-in-a-row pieces to determine a win, full board with no player winning (draw) and no win conditions - 
Input board, Output 0/1/2/3 (0 no win/draw, 1 p1 win, 2 p2 win, 3 draw)

5) apply_move - Applies player's move with row, column and rotational index onto the board with 1 or 2 depending on p1 or p2 turn - 
Input board, turn, row, col, rot, Output board

6) computer_move - Computer player that can be assigned to play against human player or ...... itself. A.I. level 1 randomly places pieces on the board, level 2 randomly places pieces on the board but a win condition will happen on the next turn, A.I will take necessary measures to stop opponent from winning/allow itself to win - 
Input board, turn, level, Output row, col, rot

7) display_board - Visualisation of board on a tkinter window, buttons to close window and print row, col and rot with respect to the piece clicked -
Input board, Outputs nothing

8) menu - Handles all the functions with the user's inputs and outputs nothing
