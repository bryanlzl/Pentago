import numpy as np

def zerocount(board): # Count number of zeros (unoccupied positions) on the board    
    count0 = 0
    for row in board:
        for col in row:
            if col == 0:
                count0 += 1
    return count0

def onecount(board): # Count number of one (P1 positions) on the board
    count1 = 1
    for row in board:
        for col in row:
            if col == 1:
                count1 += 1
    return count1

def twocount(board): # Count number of two (P2 pieces positions) on the board
    count2 = 2
    for row in board:
        for col in row:
            if col == 2:
                count2 += 1
    return count2

def check_turn(board, turn): # Takes nonzeros on the board and determines whose turn is next
    current_turn = onecount(board) + twocount(board)
    if turn == 1 or turn == 2:
        if current_turn == 0:
            if turn == 1:
                return True     
        elif (current_turn % 2) - (turn % 2) == 0: # Odd nonzero number = player 1, Even nonzero turn = player 2
            return True
    else:
        return False
    
def check_move(board,row,col): # PROJECT SKELETON FUNCTION (check_move(board,row,col))
    if 0 <= row <= 5:
        if 0 <= col <= 5:
            if board[row][col] == 0:
                return True
    else:
        return False

def rotation(board,rot): # Takes a board array and rotate it with the respective rotation ID
    if rot == 1 or rot == 2: ### ROTATIONAL ID 1/2 ### referring to the top right quadrant   
        n_col,n_row,n_col_st = 6,0,3       
        count,n,nn = 0,0,1      
        rotid,q1 = [],[]
        q1u = [list(board[n_row][n_col_st:n_col]),list(board[n_row+1][n_col_st:n_col]),list(board[n_row+2][n_col_st:n_col])]
        for i in q1u:
            q1.extend(i) # adds each list of each horizontal row of pieces into into list, q1
        while count <= 8: # putting the coordinates of each piece on the board from left to right, top to bottom order in a list 'rotid'
                if (n_col-nn) <= 1:
                    if (n_row+n) <= 2:
                        a = [nc+n,n_col-nn] #cooridinates of player's pieces
                        rotid.append(a) 
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0
                elif (n_col-nn) <= 2:
                    if (n_row+n) <= 2:
                        b = [n_row+n,n_col-nn]
                        rotid.append(b)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0
                else:
                    if (n_row+n) <= 2:
                        c = [n_row+n,n_col-nn]
                        rotid.append(c)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0
        if rot % 2 != 0: # if odd int rot, clockwise rotation
            q1index = 0
            for i in rotid:
                board[i[0]][i[1]] = q1[q1index]
                q1index += 1
        elif rot % 2 == 0: # if even int rot, anti-clockwise rotation
            rotid.reverse() # anti-clockwise is reverse of clockwise
            q1index = 0
            for i in rotid:
                board[i[0]][i[1]] = q1[q1index]
                q1index += 1
    elif rot == 3 or rot == 4: ### ROTATIONAL ID 3/4 ### refers to row and col of range(3,6)
        n_col,n_row,n_col_st = 6,3,3
        count,n,nn = 0,0,1
        rotid,q1 = [],[]
        q1u = [list(board[n_row][n_col_st:n_col]),list(board[n_row+1][n_col_st:n_col]),list(board[n_row+2][n_col_st:n_col])]
        for i in q1u:
            q1.extend(i) # putting the coordinates of each piece on the board from left to right, top to bottom order in a list 'rotid'
        while count <= 8:
                if (n_col-nn) <= 1:
                    if (n_row+n) <= 5:
                        a = [n__row+n,n_col-nn]
                        rotid.append(a)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0
                elif (n_col-nn) <= 2:
                    if (n_row+n) <= 5:
                        b = [n_row+n,n_col-nn]
                        rotid.append(b)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0
                else:
                    if (n_row+n) <= 5:
                        c = [n_row+n,n_col-nn]
                        rotid.append(c)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0            
        if rot % 2 != 0: # if rot is odd number, clockwise
            q1index = 0
            for i in rotid:
                board[i[0]][i[1]] = q1[q1index]
                q1index += 1
        elif rot % 2 == 0: # if rot is even number, anti-clockwise
            rotid.reverse() # anti-clockwise is reverse of clockwise
            q1index = 0
            for i in rotid:
                board[i[0]][i[1]] = q1[q1index]
                q1index += 1
    elif rot == 5 or rot == 6: ### ROTATIONAL ID 5/6 ###      
        n_col,n_row,n_col_st = 3,3,0
        count,n,nn = 0,0,1      
        rotid,q1 = [],[] 
        q1u = [list(board[n_row][n_col_st:n_col]),list(board[n_row+1][n_col_st:n_col]),list(board[n_row+2][n_col_st:n_col])]
        for i in q1u:
            q1.extend(i)
        while count <= 8:
                if (n_col-nn) <= 2:
                    if (n_row+n) <= 5: # rearrangement of coordinates to rotate using a specific pattern
                        a = [n_row+n,n_col-nn]
                        rotid.append(a)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0
                elif (n_col-nn) <= 1:
                    if (n_row+n) <= 5: # rearrangement of coordinates to rotate using a specific pattern
                        b = [n_row+n,n_col-nn]
                        rotid.append(b)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0
                else:
                    if (n_row+n) <= 5: # rearrangement of coordinates to rotate using a specific pattern
                        c = [n_row+n,n_col-nn]
                        rotid.append(c)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0
        if rot % 2 != 0: # if odd int rot, rotate clockwise
            q1index = 0
            for i in rotid:
                board[i[0]][i[1]] = q1[q1index]
                q1index += 1  
        elif rot % 2 == 0: # if even int rot, rotate anti-clockwise
            rotid.reverse() # anti-clockwise is reverse clockwise
            q1index = 0
            for i in rotid:
                board[i[0]][i[1]] = q1[q1index]
                q1index += 1
    elif rot == 7 or rot == 8: ### ROTATIONAL ID 7/8 ###
        n_col,n_row,n_col_st = 3,0,0 
        count,n,nn = 0,0,1
        rotid,q1 = [],[]
        q1u = [list(board[n_row][n_col_st:n_col]),list(board[n_row+1][n_col_st:n_col]),list(board[n_row+2][n_col_st:n_col])]
        for i in q1u: # adds each list of each horizontal row of pieces into into list, q1
            q1.extend(i) # putting the coordinates of each piece on the board from left to right, top to bottom order in a list 'rotid'
        while count <= 8:
                if (n_col-nn) <= 1:
                    if (n_row+n) <= 2: # rearrangement of coordinates to rotate using a specific pattern
                        a = [n_row+n,n_col-nn]
                        rotid.append(a)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0
                elif (n_col-nn) <= 2:
                    if (n_row+n) <= 2: # rearrangement of coordinates to rotate using a specific pattern
                        b = [n_row+n,n_col-nn]
                        rotid.append(b)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0
                else:
                    if (n_row+n) <= 2: # rearrangement of coordinates to rotate using a specific pattern
                        c = [n_row+n,n_col-nn] 
                        rotid.append(c)
                        n += 1
                        count += 1
                        continue
                    nn += 1
                    n = 0    
        if rot % 2 != 0: # if odd int rot, rotate clockwise
            q1index = 0
            for i in rotid:
                board[i[0]][i[1]] = q1[q1index]
                q1index += 1
        elif rot % 2 == 0: # if even int rot, rotate anti-clockwise
            rotid.reverse() # anti-clockwise is reverse clockwise
            q1index = 0
            for i in rotid:
                board[i[0]][i[1]] = q1[q1index]
                q1index += 1
    else:
        return board # INVALID ROTATION ID!

def victory_board(board):
    winposlist = [[],[],[],[],[],[]]   # OVERALL FUNCTION LIST
    win1count,win2count,count,out_return0,out_return1,out_return2,out_return3 = 0,0,0,0,0,0,0
    ddid0,ddid1,ddid4,ddid5,decrid5,incrid0,ddcount,dcount= 0,1,4,5,5,0,0,0  # FOR DIAGDIAG & DIAG POSSIBILITIES
    vcount,hcount,vrow,hcol,vlist,hlist = 0,0,0,0,[],[]    # FOR VERTICAL & HORIZONTAL POSSIBILITIES
    # DIAGONAL-DIAGONAL
    while ddcount < 5:
        winposlist[0].append(board[ddid0][ddid1])
        winposlist[1].append(board[ddid1][ddid0])
        winposlist[2].append(board[ddid4][ddid0])
        winposlist[3].append(board[ddid5][ddid1])
        ddid0 += 1
        ddid1 += 1
        ddid4 -= 1
        ddid5 -= 1
        ddcount += 1
    # DIAGONAL        
    while dcount < 6:
        winposlist[4].append(board[incrid0][incrid0])
        winposlist[5].append(board[decrid5][incrid0])
        incrid0 += 1
        decrid5 -= 1
        dcount += 1
    #VERTICAL
    while vcount < 36:
        vlist.append(board[vrow][vcount//6])
        vcount += 1
        vrow += 1
        if vrow == 6:
            vrow = 0
            winposlist.append(vlist)
            vlist = []
   # HORIZONTAL         
    while hcount < 36:
        hlist.append(board[hcount//6][hcol])
        hcount += 1
        hcol += 1
        if hcol == 6:
            hcol = 0
            winposlist.append(hlist)
            hlist = []   
    ############### WIN CHECKER ################
    while count < len(winposlist): #Stacking up the '1's and '2's for a win/draw condition
        win1count = 0
        win2count = 0
        for i in winposlist[count]:
            if i == 1:
                win1count += 1
                if win1count >= 5: # win condition
                    out_return1 = 1
            elif i != 1:
                win1count = 0 
        for i in winposlist[count]:
            if i == 2:
                win2count += 1
                if win2count >= 5: # win condition
                    out_return2 = 2 
            elif i != 2:
                win2count = 0
        count += 1
    if np.count_nonzero(board) == 36:
        if (out_return1 + out_return2) == 3:
            return 3
        elif (out_return1 + out_return2) == 1:
            return 1
        elif (out_return1 + out_return2) == 2:
            return 2
        else:
            return 3
    elif np.count_nonzero(board) < 36: #Returning outputs
        if (out_return1 + out_return2) == 3:
            return 3
        elif (out_return1 + out_return2) == 1:
            return 1
        elif (out_return1 + out_return2) == 2:
            return 2
        else:
            return 0
        
def check_victory(board,turn,rot): # PROJECT SKELETON FUNCTION (check_victory(board,turn,rot))
    row = board.shape[0]
    col = board.shape[1]
    vboard = np.zeros((row,col))
    for i in range(row):
        for j in range(col):
            vboard[i,j]=board[i,j]
    if victory_board(vboard) == 1 or victory_board == 2:
        return victory_board(vboard)
    else:
        rotation(vboard,rot)
        return victory_board(vboard)

def apply_move(board,turn,row,col,rot): # PROJECT SKELETON FUNCTION (apply_move(board,turn,row,col,rot))
    if check_turn(board,turn):
        if check_move(board,row,col):
            if 1 <= rot <= 8:
                if turn == 1: # PLYAER 1 TURN
                    board[row][col] = 1
                    if victory_board(board) > 0:
                        ##### WIN/DRAW #####
                        return board    
                    rotation(board,rot)   
                    if victory_board(board) == 0:
                        ##### NO CONCLUSION HERE #####
                        pass
                    else:
                        ##### WIN/DRAW #####
                        return board
                elif turn == 2: # PLAYER 2 TURN
                    board[row][col] = 2
                    if victory_board(board) > 0:
                        ##### WIN/DRAW #####
                        return board   
                    rotation(board,rot) 
                    if victory_board(board) == 0:
                        ##### NO CONCLUSION HERE #####
                        pass
                    else:
                        ##### WIN/DRAW #####
                        return board
            else:
                return board # INVALID ROTATION ID!
        else:
            return board # INVALID MOVE!
    else:
        return board # INVALID TURN!
    return board

def computer_move(board,turn,level): # PROJECT SKELETON FUNCTION (computer_move(board,turn,level))
    import random
    ai_row,ai_col = 0,0
    
    if level == 1:
        ai_row = random.randint(0,5)
        ai_col = random.randint(0,5)
    
        while 1==1:
            ai_row = random.randint(0,5)
            ai_col = random.randint(0,5)
            if check_move(board,ai_row,ai_col) == True:
                break
        ai_rot = random.randint(1,8)
        return ai_row,ai_col,ai_rot
    
    if level == 2:
        op_turn,opp_win_pos,op_windicator,ai_row,ai_col,ai_rot,sai_rot = 0,0,0,0,0,8,8
        row,col = board.shape[0],board.shape[1]
        pvboard = np.zeros((row,col)) # empty test board container
        oppvboard = np.zeros((row,col)) # empty 'prevent enemy wins' test board
        # Finding opponent's turn #
        if turn % 2 == 0:
            op_turn = turn - 1
        else:
            op_turn = turn + 1
            
        for i in range(row):
            for j in range(col):
                for rrow in range(row): # Creates a 'test' board from game board, pvboard, to test/simulate win conditions
                    for ccol in range(col): # Creating pvboard
                        pvboard[rrow,ccol] = board[rrow,ccol] # pvboard replicated from game board
                        
        # AI IMMEDIATE PIECE WIN (NO NEED BOTHER ROTATION) #
                if check_move(pvboard,i,j):
                    pvboard[i][j] = turn
                    if victory_board(pvboard) == turn:
                        ai_row,ai_col = i,j
                        return ai_row,ai_col,ai_rot # RRRREEEETTTTUUUURRRRNNNN  
                    
                # AI NO PIECE WIN BUT ROTATE WIN #            
                    elif victory_board(pvboard) == 0:
                        for rot in range(1,sai_rot+1):
                            rotation(pvboard,rot)
                            if victory_board(pvboard) == turn:
                                ai_row,ai_col = i,j
                                return ai_row,ai_col,rot # RRRREEEETTTTUUUURRRRNNNN  
                            rotation(pvboard,rot)
                            rotation(pvboard,rot)
                            rotation(pvboard,rot)
        
        # ONCE THERE ARE NO DIRECT WIN POSSIBLITIES FOR AI #
        # CHECK IF OPPONENT CAN DIRECT WIN #   
        for i in range(row):
            for j in range(col):
                for rrow in range(row):
                    for ccol in range(col):
                        pvboard[rrow,ccol] = board[rrow,ccol]
                if check_move(pvboard,i,j):
                    pvboard[i][j] = op_turn
                    if victory_board(pvboard) == op_turn:
                        opp_win_pos = 1                   # Opp can direct win next turn
                        break         
                    elif victory_board(pvboard) == 0:
                        for rot in range(1,sai_rot+1):
                            rotation(pvboard,rot)
                            if victory_board(pvboard) == op_turn:
                                opp_win_pos = 1           # Opp can direct win next turn
                                break
                            rotation(pvboard,rot)
                            rotation(pvboard,rot)
                            rotation(pvboard,rot)
                            
        # CHECK FOR OPPONENT'S WIN POSSIBILITIES #  
        if opp_win_pos == 1: 
            for i in range(row):
                for j in range(col):
                    for rrow in range(row):
                        for ccol in range(col):
                            pvboard[rrow,ccol] = board[rrow,ccol]
                    if check_move(pvboard,i,j):
                        pvboard[i][j] = turn
                        for rot in range(1,sai_rot+1):
                            rotation(pvboard,rot)        
                            # SIMULATE ENEMY PIECE, ROTATE AND CHECK IF ANY WIN #
                            # Whatever piece and/or rotate that AI puts to prevent a win outcome will be CHOSEN! #
                            op_windicator = 0 # Stands for Opponent Win Indicator, 0 means cannot win anymore, 1 means can win
                            for opi in range(row):
                                for opj in range(col):
                                    for rrow in range(row): # Creates another test board specifically to simulate all possible enemy moves
                                        for ccol in range(col): # 'opponent victory board' in short
                                            oppvboard[rrow,ccol] = pvboard[rrow,ccol] # oppvboard replicated from pvboard
                                    if check_move(oppvboard,opi,opj):
                                        oppvboard[opi][opj] = op_turn
                                        if victory_board(oppvboard) == op_turn or victory_board(oppvboard) == 3: #check for opp win when put piece
                                            op_windicator = 1
                                        for oprot in range(1,sai_rot+1): 
                                            rotation(oppvboard,oprot)
                                            if victory_board(oppvboard) == op_turn or victory_board(oppvboard) == 3: #check for opp win after rotation
                                                op_windicator = 1 
                                            rotation(oppvboard,oprot)
                                            rotation(oppvboard,oprot)
                                            rotation(oppvboard,oprot)
                            if op_windicator == 0: # IF OPP CANNOT WIN AFTER AI APPLIES MOVE, AI will use that moveset (to prevent opp's direct win!)
                                ai_row,ai_col = i,j
                                return(ai_row,ai_col,rot) # RRRREEEETTTTUUUURRRRNNNN  
                             # END OF OPPONENT MOVESET SIMULATION FOR CURRENT AI MOVESET #
                            rotation(pvboard,rot)
                            rotation(pvboard,rot)
                            rotation(pvboard,rot)  
                            
            if op_windicator == 1: #if reallly no way for AI to prevent OPP win, GENERATE RANDOM MOVESET  
                ai_row = random.randint(0,5)
                ai_col = random.randint(0,5)
                while 1==1:
                    ai_row = random.randint(0,5)
                    ai_col = random.randint(0,5)
                    if check_move(board,ai_row,ai_col) == True:
                        break
                ai_rot = random.randint(1,8)
                return ai_row,ai_col,ai_rot # RRRREEEETTTTUUUURRRRNNNN  

        #if no near win or lose conditions for either side, randomly put pieces and random rotate on the board#
        elif opp_win_pos == 0:
            ai_row = random.randint(0,5)
            ai_col = random.randint(0,5)
            while 1==1:
                ai_row = random.randint(0,5)
                ai_col = random.randint(0,5)
                if check_move(board,ai_row,ai_col) == True:
                    break
            ai_rot = random.randint(1,8)
            return ai_row,ai_col,ai_rot # RRRREEEETTTTUUUURRRRNNNN  

def display_board(board): # PROJECT SKELETON FUNCTION (display_board(board))
    import tkinter # Python GUI library
    roww,coll = 0,0
    pentago = tkinter.Tk() ########### START WINDOW LOOP ############
    pentago.geometry('600x356') # Sets dimensions of window interface when opened
    # LAMBDA allows tkinter button to execute command ONLY ON CLICK (basically a temporary function)
    # Buttons will print their respective row, col and rotation on the console upon click
    # .place() is used to manually position a button on the window interface
    close_window = tkinter.Button(pentago, text='Next Player' , bg = 'gray', width = 10, height = 3, font=("Arial", 16), command=pentago.destroy).place(x=410, y=250)
    # close_window is a button displays next player, closes the window to allow next window and proceeding codelines to run in menu()
    getrow = tkinter.Button(pentago, text= ' CL1 , AT2 ', bg = 'yellow', command =  lambda: print('clockwise rot 1, Anti-clockwise rot 2')).place(x=530, y=60)
    getcol = tkinter.Button(pentago, text = ' CL3 , AT4 ', bg = 'yellow', command =  lambda: print('clockwise rot 3, Anti-clockwise rot 4')).place(x=530, y=180)
    getrot = tkinter.Button(pentago, text = ' CL7 , AT8 ', bg = 'yellow', command =  lambda: print('clockwise rot 7, Anti-clockwise rot 8')).place(x=360, y=60)
    getrot = tkinter.Button(pentago, text = ' CL5 , AT6 ', bg = 'yellow', command = lambda: print('clockwise rot 5, Anti-clockwise rot 6')).place(x=360, y=180)
    for i in board: # Creating a series of buttons on the board named 'Pentag', which will be the visual representation
        for j in i: # -of the board and for loop to loop through all board pieces
            
            if j == 0: # Unoccupied position on board will be represented in white, with '%' used to assign row and col index
                        # and display on unoccupied position buttons.           
                        # these buttons prints row and col on click
                pentag = tkinter.Button(text = "%s,%s" % (roww//6, coll), fg = 'black', bg = 'white', width = 7, height = 3, command = lambda row=roww// 6, col=coll: print('Piece has row',row,'and col',col))
                pentag.grid(row = roww//6, column = coll) # Grid function used to create a grid of 6x6 button set
            
            elif j == 1: # player 1 position on board, DISPLAYED IN BLUE
                pentag = tkinter.Button(fg = 'black', bg = 'blue', width = 7, height = 3)
                pentag.grid(row = roww//6, column = coll)
           
            elif j == 2: # player 2 position on board, DISPLAYED IN RED
                pentag = tkinter.Button(fg = 'black', bg = 'red', width = 7, height = 3)
                pentag.grid(row = roww//6, column = coll)
                
            coll += 1
            roww += 1
            if coll == 6:
                coll = 0    
                
    pentago.mainloop()  ###### END WINDOW LOOP ######
    
def menu(): # # PROJECT SKELETON FUNCTION (menu())
    import numpy as np
    board = np.zeros((6,6))
    while 1: # Entire function will run till a return condition ends the loop
        whattodo = str(input("Welcome to Pentago!\nTo play Human(P1) vs Human(P2), enter 'hh'\nTo play Human(P1) vs A.I.(P2), enter 'ha'\nTo play A.I.(P1) vs Human(P2) enter 'ah'\nTo watch A.I.(P1) vs A.I.(P2) enter 'aa'\nTo exit game, enter 'e'\n"))
        board = np.zeros((6,6))
        # Interacts with user by asking for which game mode to play
        ##### Human vs Human #####
        if whattodo == 'hh':
            print("Welcome! To go back to menu, enter '9' when inputting row, col and rot!")
            while 1:
                try: # HUMAN PLAYER 1 MOVES
                    row,col,rot = int(input('Row?: ')),int(input('Col?: ')),int(input('Rotation?: '))
                except:
                    continue
                if row == 9: # by keying 9 for row,col,rot, allows plyer to return to menu
                    break
                if col == 9:
                    break
                if rot == 9:
                    break    
                apply_move(board,1,row,col,rot)
                print('Player 1 moved')
                display_board(board)
                if victory_board(board) > 0: # If any win or draw conditions, THIS MODE WILL TERMINATE and return to menu
                    if victory_board(board) == 1:
                        print('Winner is player',1)
                        break
                    elif victory_board(board) == 2:
                        print('Winner is player',2)
                        break
                    elif victory_board(board) == 3:
                        print("It's a draw!")
                        break
                try: # HUMAN PLAYER 2 MOVES
                    row,col,rot = int(input('Row?: ')),int(input('Col?: ')),int(input('Rotation?: '))
                except:
                    continue
                if row == 9: # by keying 9 for row,col,rot, allows plyer to return to menu
                    break
                if col == 9:
                    break
                if rot == 9:
                    break    
                apply_move(board,2,row,col,rot)
                print('Player 2 moved')
                display_board(board)
                if victory_board(board) > 0: # If any win or draw conditions, THIS MODE WILL TERMINATE and return to menu
                    if victory_board(board) == 1:
                        print('Winner is player',1)
                        break
                    elif victory_board(board) == 2:
                        print('Winner is player',2)
                        break
                    elif victory_board(board) == 3:
                        print("It's a draw!")
        
        ##### Human vs A.I. #####
        elif whattodo == 'ha':
            while 1:
                try:
                    level = int(input('AI level of P2? 1/2: '))
                    if level in [1,2]:
                        break # once level is within the parameters of 1 and 2, proceed to next while loop after break
                except:
                    continue # any errors, repeat int(input())
            ai_move = ()
            print("Welcome! To go back to menu, enter '9' when inputting row, col and rot!")
            while 1:
                try: # HUMAN PLAYER 1 MOVES
                    row,col,rot = int(input('Row?: ')),int(input('Col?: ')),int(input('Rotation?: '))
                except:
                    continue
                if row == 9: # by keying 9 for row,col,rot, allows plyer to return to menu
                    break
                if col == 9:
                    break
                if rot == 9:
                    break
                apply_move(board,1,row,col,rot)
                print('Player 1 moved')
                display_board(board)
                if victory_board(board) > 0: # If any win or draw conditions, THIS MODE WILL TERMINATE and return to menu
                    if victory_board(board) == 1:
                        print('Winner is player',1)
                        break
                    elif victory_board(board) == 2:
                        print('Winner is A.I. player',2)
                        break
                    elif victory_board(board) == 3:
                        print("It's a draw!")
                        break
                ai_move = computer_move(board,2,level) # AI PLAYER 2 MOVES
                row,col,rot = ai_move[0],ai_move[1],ai_move[2]
                apply_move(board,2,row,col,rot)
                print('A.I. (player 2) moved')
                display_board(board)
                if victory_board(board) > 0: # If any win or draw conditions, THIS MODE WILL TERMINATE and return to menu
                    if victory_board(board) == 1:
                        print('Winner is player',1)
                        break
                    elif victory_board(board) == 2:
                        print('Winner is A.I. player',2)
                        break
                    elif victory_board(board) == 3:
                        print("It's a draw!")
                        break
                
        ###### A.I. vs Human ######
        elif whattodo == 'ah':
            while 1:
                try:
                    level = int(input('AI level of P1? 1/2: '))
                    if level in [1,2]:
                        break # once level is within the parameters of 1 and 2, proceed to next while loop after break
                except:
                    continue # any errors, repeat int(input())
            ai_move = ()
            print("Welcome! To go back to menu, enter '9' when inputting row, col and rot!")
            while 1:
                ai_move = computer_move(board,1,level) # AI PLAYER 1 MOVES
                row,col,rot = ai_move[0],ai_move[1],ai_move[2]
                apply_move(board,1,row,col,rot)
                print('A.I. (player 1) moved')
                display_board(board)
                if victory_board(board) > 0: # If any win or draw conditions, THIS MODE WILL TERMINATE and return to menu
                    if victory_board(board) == 1:
                        print('Winner is A.I. player',1)
                        break
                    elif victory_board(board) == 2:
                        print('Winner is player',2)
                        break
                    elif victory_board(board) == 3:
                        print("It's a draw!")
                        break
                try: # HUMAN PLAYER 2 MOVES
                    row,col,rot = int(input('Row?: ')),int(input('Col?: ')),int(input('Rotation?: '))
                except:
                    continue
                if row == 9: # by keying 9 for row,col,rot, allows plyer to return to menu
                    break
                if col == 9:
                    break
                if rot == 9:
                    break
                apply_move(board,2,row,col,rot)
                print('Player 2 moved')
                display_board(board)
                if victory_board(board) > 0: # If any win or draw conditions, THIS MODE WILL TERMINATE and return to menu
                    if victory_board(board) == 1:
                        print('Winner is A.I. player',1)
                        break
                    elif victory_board(board) == 2:
                        print('Winner is player',2)
                        break
                    elif victory_board(board) == 3:
                        print("It's a draw!")
                        break
                        
        ##### A.I. VS A.I. SPECTATOR MODE! #####        
        elif whattodo == 'aa':
            while 1:
                try:
                    levela1 = int(input('AI level of P1? 1/2: '))
                    levela2 = int(input('AI level of P2? 1/2: '))
                    if levela1 in [1,2] and levela2 in [1,2]:
                        break # once both are within the parameters of 1 and 2, proceed to next while loop after break
                except:
                    continue # any errors, repeat int(input())
            rmenu_counter = 0
            while 1:
                ai_move = computer_move(board,1,levela1) # AI PLAYER 1 MOVES
                row,col,rot = ai_move[0],ai_move[1],ai_move[2]
                apply_move(board,1,row,col,rot)
                print('A.I. (player 1) moved')
                display_board(board)
                if victory_board(board) == 1: # If any win or draw conditions, THIS MODE WILL TERMINATE and return to menu
                    print('Winner is A.I. player',1)
                    break
                elif victory_board(board) == 2:
                    print('Winner is A.I. player',2)
                    break
                elif victory_board(board) == 3:
                    print("It's a draw!")
                    break             
                ai_move = computer_move(board,1,levela2) # AI PLAYER 2 MOVES
                row,col,rot = ai_move[0],ai_move[1],ai_move[2]
                apply_move(board,2,row,col,rot)
                print('A.I. (player 2) moved')
                display_board(board)
                if victory_board(board) == 1: # If any win or draw conditions, THIS MODE WILL TERMINATE and return to menu
                    print('Winner is A.I. player',1)
                    break
                elif victory_board(board) == 2:
                    print('Winner is A.I. player',2)
                    break
                elif victory_board(board) == 3:
                    print("It's a draw!")
                    break       
                rmenu_counter += 1 # ALLOWS VIEWER TO LEAVE ONCE EVERY 10 TURNS
                if rmenu_counter % 5 == 0:
                    menuinput = str(input('Quit to menu? y/n: '))
                    if menuinput == 'y':
                        break
        elif whattodo == 'e': # EXITS GAME, CLOSES MENU()
            return 

menu()        
