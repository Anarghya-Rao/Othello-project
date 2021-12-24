# Othello varient : Playing against automated player


import math    # For defining infinity
from copy import deepcopy


#Create board (brand-new board) with initial set-up
def create_board():
    board=[[' ','1','2','3','4','5','6','7','8',' '], [1,'-','-','-','-','-','-','-','-',1], [2,'-','-','-','-','-','-','-','-',2], [3,'-','-','-','-','-','-','-','-',3], [4,'-','-','-','O','X','-','-','-',4], [5,'-','-','-','X','O','-','-','-',5], [6,'-','-','-','-','-','-','-','-',6], [7,'-','-','-','-','-','-','-','-',7], [8,'-','-','-','-','-','-','-','-',8], [' ','1','2','3','4','5','6','7','8',' ']]            
    print()
    print('Game Board')
    print()
    for row in board:
        for col in row:
            print(col,end=' ')      
        print()
    print()
    print("Note:","\'-\' denote empty spaces",
          "\'X\' denotes black coins (Player 1)",
          "\'O\' denotes white coins (Player 2)",
          "\'1,2,3...\' denote row/coloumn numbers",sep='\n')
    print()
    print()
    return board

# Display_board function
# Just displays the current board situation
# So that player can see the board and make their required move.
def display_board(board):
    for row in board:                                       
        for col in row:
            print(col,end=' ')      
        print()
                    
def create_pos_list(board,sym): 
    #First, generate list of moves for that symbol
    pos_list=[]
    temp=[]
    if sym=='X':
        oppnt='O'
    else:
        oppnt='X'
    #for r in range(1,9):
    #for c in range(1,9):     #Range such that only board is considered, outer position numbers are not.
    for r in range(1,9):
        for c in range(1,9):
            if (board[r][c]=='-'):      #Thus, doesn't take positions that are occupied
                any_of_eight=check_eight(board,r,c,oppnt) #function returns T/F #if even one cell(of eight) is oppnt(opponent),returns true,else false.
                if any_of_eight:
                    temp.append((r,c))
    for loc in temp:
        if check_if_turn(board,loc[0],loc[1],oppnt,sym):  #function returns T/F 
            pos_list.append(loc)    #Will have the absolute final list of all the possible (all conditions checked) pos for that symbol.

    
    return pos_list
                

# Function: check_eight. 
# check the eight locations with extra condition to prune out and get a smaller list of possibilities. then every pos checked for turning using another function.
# Extra condition: all eight empty or with player's symbol, then skip.
def check_eight(board,r,c,oppnt): 
    if (board[r-1][c]==oppnt) or (board[r-1][c+1]==oppnt) or (board[r][c+1]==oppnt) or (board[r+1][c+1]==oppnt) or (board[r+1][c]==oppnt) or (board[r+1][c-1]==oppnt) or (board[r][c-1]==oppnt) or (board[r-1][c-1]==oppnt): 
        return True   
    else:
        return False
    #return T/F




# Function: check_if_turn.
# If even one direction (after checking if immediate is oppnt) will lead to turning, returns true, else false.  
def check_if_turn(board,r,c,oppnt,sym): 
    if board[r-1][c]==oppnt:  
        i=r-2 
        while(board[i][c]==oppnt):   
            i=i-1  
        if board[i][c]==sym: 
            return True  
    if board[r-1][c+1]==oppnt:    
        i,j=r-2,c+2
        while(board[i][j]==oppnt):
            i,j=i-1,j+1
        if board[i][j]==sym:                               
            return True  
    if board[r][c+1]==oppnt:
        j=c+2
        while(board[r][j]==oppnt):
            j=j+1
        if board[r][j]==sym:
            return True 
    if board[r+1][c+1]==oppnt:
        i,j=r+2,c+2
        while(board[i][j]==oppnt):
            i,j=i+1,j+1   
        if board[i][j]==sym:
            return True 
    if board[r+1][c]==oppnt:
        i=r+2 
        while(board[i][c]==oppnt):
            i=i+1
        if board[i][c]==sym:
            return True 
    if board[r+1][c-1]==oppnt:
        i,j=r+2,c-2
        while(board[i][j]==oppnt):
            i,j=i+1,j-1
        if board[i][j]==sym:
            return True 
    if board[r][c-1]==oppnt:
        j=c-2
        while(board[r][j]==oppnt):
            j=j-1
        if board[r][j]==sym:
            return True 
    if board[r-1][c-1]==oppnt:
        i,j=r-2,c-2
        while(board[i][j]==oppnt):
            i,j=i-1,j-1
        if board[i][j]==sym:
            return True 
    else:
        return False


# Function: check_for_moves
# Sees if there are any moves at all for player, if not, must transfer turn to other player, else must allow the player to continue his turn.
def check_for_moves(pos_list):  
    if len(pos_list)==0:
        print("Player has no possible moves! Passing the play to other player.")
        print()
        return False
    else:
        return True
    
           
    
# Function: check_with_pos_list
# Checks if the move is in pos_list, only then it will be a valid move. Else must loop until valid input is given.
def check_with_pos_list(pos_list,r,c):
    move=(r,c)
    if move in pos_list:
        return True
    else:
        print("Invalid move, please try again.")
        return False
                        
# Function: turn_coins
# Turns the coins for that player's move
def turn_coins(board,r,c,sym,oppnt,sim=False):    #sim = simulation

    if sim==True:
        board=deepcopy(board)     
    if board[r-1][c]==oppnt:        
        i=r-2
        while(board[i][c]==oppnt):     
            i=i-1
        if board[i][c]==sym:
            board[r][c]=sym
            # Must turn the coins then
            a=r-1
            while(board[a][c]==oppnt):
                board[a][c]=sym
                a=a-1
                
    if board[r-1][c+1]==oppnt:
        i,j=r-2,c+2
        while(board[i][j]==oppnt):
            i,j=i-1,j+1
        if board[i][j]==sym:
            board[r][c]=sym
            # Must turn the coins then
            a,b=r-1,c+1
            while(board[a][b]==oppnt):
                board[a][b]=sym
                a,b=a-1,b+1 

    if board[r][c+1]==oppnt:
        j=c+2
        while(board[r][j]==oppnt):
            j=j+1
        if board[r][j]==sym:
            board[r][c]=sym
            # Must turn the coins then
            b=c+1
            while(board[r][b]==oppnt):
                board[r][b]=sym
                b=b+1

    if board[r+1][c+1]==oppnt:
        i,j=r+2,c+2
        while(board[i][j]==oppnt):
            i,j=i+1,j+1   
        if board[i][j]==sym:
            board[r][c]=sym
            # Must turn the coins then
            a,b=r+1,c+1
            while(board[a][b]==oppnt):
                board[a][b]=sym
                a,b=a+1,b+1

    if board[r+1][c]==oppnt:
        i=r+2 
        while(board[i][c]==oppnt):
            i=i+1
        if board[i][c]==sym:
            board[r][c]=sym
            # Must turn the coins then
            a=r+1
            while(board[a][c]==oppnt):
                board[a][c]=sym
                a=a+1

    if board[r+1][c-1]==oppnt:
        i,j=r+2,c-2
        while(board[i][j]==oppnt):
            i,j=i+1,j-1
        if board[i][j]==sym:
            board[r][c]=sym
            # Must turn the coins then
            a,b=r+1,c-1
            while(board[a][b]==oppnt):
                board[a][b]=sym
                a,b=a+1,b-1

    if board[r][c-1]==oppnt:
        j=c-2
        while(board[r][j]==oppnt):
            j=j-1
        if board[r][j]==sym:
            board[r][c]=sym
            # Must turn the coins then
            b=c-1
            while(board[r][b]==oppnt):
                board[r][b]=sym
                b=b-1 

    if board[r-1][c-1]==oppnt:
        i,j=r-2,c-2
        while(board[i][j]==oppnt):
            i,j=i-1,j-1
        if board[i][j]==sym:
            board[r][c]=sym
            # Must turn the coins then
            a,b=r-1,c-1
            while(board[a][b]==oppnt):
                board[a][b]=sym
                a,b=a-1,b-1 
    if sim==False:
        print("Turned! Updated board:")        
    return board
    
                    

# Function: check_endgame
# Game ends if:
    # neither players have moves
         # ie create_pos_list for both (use 'and') symbols give empty lists
# Then must check who won (by counting no. of cells for each player and then declare winner with score).
def check_endgame(board,sym1,sym2):
    l1=create_pos_list(board,sym1)
    l2=create_pos_list(board,sym2)
    if(len(l1)==0 and len(l2)==0):   #Only if both pos_lists are empty, game over
        print("Players have no more moves! Game over.")
        return 1
    else:
        return 0
        

# Function: check_winner
# Checks who won by counting no. of coins of each player on board and then declares winner (whoever with higher coin count) with their coin counts.
def check_winner(board,sym1,sym2,P1,P2="Computer"):
    sym1_count=0
    sym2_count=0
    for r in range(1,9):
        for c in range(1,9):
            if board[r][c]==sym1:
                sym1_count+=1
            elif board[r][c]==sym2:
                sym2_count+=1
    if sym1_count>sym2_count:
        print("Scores:")
        print("Number of Player 1 coins: ",sym1_count)
        print("Number of Player 2 coins: ",sym2_count)
        print("Player 1,",P1,"wins!!")
    elif sym2_count>sym1_count:
        print("Scores:")
        print("Number of Player 1 coins: ",sym1_count)
        print("Number of Player 2 coins: ",sym2_count)
        print("Player 2, Computer wins!!")
    else:               
        print("Scores:")
        print("Number of Player 1 coins: ",sym1_count)
        print("Number of Player 2 coins: ",sym2_count)
        print("It's a tie!!")
            


def get_score(board):      
    sym1_score=0
    sym2_score=0
    for r in range(1,9):
        for c in range(1,9):
            if board[r][c]=='X':
                if (r,c) in [(1,1),(1,8),(8,8),(8,1)]:  #Bonus points for corners
                    sym1_score+=1000
                elif (r,c) in [(1,4),(1,5),(4,1),(5,1),(8,4),(8,5),(4,8),(5,8)]:    #Bonus points for edges
                    sym1_score+=10
                elif (r,c) in [(2,1),(2,2),(1,2),(1,7),(2,7),(2,8),(7,1),(7,2),(8,2),(7,7),(7,8),(8,7)]:  #Subtracting points for X,C positions on board
                    sym1_score-=20
                elif (r,c) in [(3,1),(3,2),(3,3),(2,3),(1,3),(1,6),(2,6),(3,6),(3,7),(3,8),(6,1),(6,2),(6,3),(7,3),(8,3),(6,6),(6,7),(6,8),(7,6),(8,6)]: #Bonus points 
                    sym1_score+=15                                                                                        #for positions adjacent to the X,C positions.
                else:       #Every other position
                    sym1_score+=1      
            elif board[r][c]=='O':
                if (r,c) in [(1,1),(1,8),(8,8),(8,1)]:  #Bonus points for corners
                    sym2_score+=1000
                elif (r,c) in [(1,4),(1,5),(4,1),(5,1),(8,4),(8,5),(4,8),(5,8)]:    #Bonus points for edges
                    sym2_score+=10
                elif (r,c) in [(2,1),(2,2),(1,2),(1,7),(2,7),(2,8),(7,1),(7,2),(8,2),(7,7),(7,8),(8,7)]:  #Subtracting points for X,C positions on board
                    sym2_score-=20
                elif (r,c) in [(3,1),(3,2),(3,3),(2,3),(1,3),(1,6),(2,6),(3,6),(3,7),(3,8),(6,1),(6,2),(6,3),(7,3),(8,3),(6,6),(6,7),(6,8),(7,6),(8,6)]: #Bonus points
                    sym2_score+=15                                                                                       #for positions adjacent to the X,C positions.
                else:       #Every other position
                    sym2_score+=1      
    return sym2_score-sym1_score       # More +ve value indicates computer winning and more -ve value indicates player winning           


def minimax_max_node(board, depth, alpha, beta):
    cur_max = -math.inf      #-infinity    
    copy_board = deepcopy(board)    
    moves = create_pos_list(board,'O')
    if len(moves)==0 or depth==0:
        return (-1,-1),get_score(board)
    else: 
        for i in moves:
            copy_board = turn_coins(board,i[0],i[1],'O','X',True)  
            new_move, new_score = minimax_min_node(copy_board, depth - 1, alpha, beta)
            if new_score > cur_max:
                cur_max = new_score
                best_move = i
            alpha = max(new_score, alpha) 
            if beta <= alpha:
                break
        return best_move, cur_max



def minimax_min_node(board, depth, alpha, beta):
    cur_min = math.inf
    copy_board = deepcopy(board)    
    moves = create_pos_list(board, 'X')
    if len(moves)==0 or depth==0:
        return (-1,-1), get_score(board)
    else: 
        for i in moves:
            copy_board = turn_coins(board,i[0],i[1],'X','O',True)
            new_move, new_score = minimax_max_node(copy_board, depth - 1, alpha, beta)
            if new_score < cur_min:
                cur_min = new_score
                best_move = i
            beta = min(new_score, beta) 
            if beta <= alpha:
                break
        return best_move, cur_min 
    



# Given a board and a player color, decide on a move. 
# The return value is a tuple of integers (i,j), where
# i is the row and j is the column on the board.  
def auto_move_minimax(board):
    best_move, score = minimax_max_node(board, 4, -math.inf, math.inf)   
    return best_move



# Play game
def play():
    print("Let's Play!")
    P1=input("Enter Player 1 name: Black (X): ")
    sym1='X'
    print("Player 2: White (O): Computer")
    sym2='O'
    board=create_board()    
    # Shows * * * * as if loading
    print("Setting up game")
    for times in range(4):
        for delay in range(10000000):
            if delay==5000000:
                #print(' '*1,'*',end='')
                print('*',end='  ')
    #End loading sequence
    print()
    print()
    turn=0
    while(1):
        #Player1
        if turn%2==0:
            pos_list=create_pos_list(board, sym1)   
            print("Player 1:",P1,"'s (X) turn:")          
            checking=check_for_moves(pos_list)
            if checking==True:
                print()
                display_board(board)
                print()
                while(1):
                    row,column=input("Enter move:(format:row column) ").split()
                    row,column=int(row),int(column)
                    correct=check_with_pos_list(pos_list,row,column)    
                    if correct:
                            break
                board=turn_coins(board,row,column,sym1,sym2)  
                display_board(board)   #Shows players updated board
                print()
                #Board displayed
                #Move checked and turned
                #Board updated and displayed
            option=int(input("(Press 1 to continue the game and 0 to quit) "))
            print()
            end=check_endgame(board,sym1,sym2)        
            if (end==1 or option==0):
                check_winner(board,sym1,sym2,P1)      
                print()
                print("Thank you for playing!")
                break
                

        #Player2
        else:     
            print("Player 2: Computer's (O) turn:")           
            print()
            display_board(board)
            print()
            print("Computing move")
            move=auto_move_minimax(board)
            row,column=move[0],move[1]
            if row==-1 and column==-1:
                print("Computer has no possible moves! Passing the play to player.")
                print()    
            else:
                board=turn_coins(board,row,column,sym2,sym1)  #Turns the coins based on selected move.  
                print("Move played:",row, column)
                print()
                display_board(board)   #Shows the updated board (ie with computer's move)
                print()
                #Board displayed
                #Move checked and turned
                #Board updated and displayed
            option=int(input("(Press 1 to continue the game and 0 to quit) "))
            print()
            end=check_endgame(board,sym1,sym2)
            if (end==1 or option==0):
                check_winner(board,sym1,sym2,P1)
                print()
                print("Thank you for playing!")
                break
            
        turn+=1                

