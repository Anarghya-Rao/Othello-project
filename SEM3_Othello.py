# Sem 3 Mini-project
# Program for game "Othello"
# Author: Anarghya Rao , 3rd sem , section A , USN: 1NH19IS012

import SEM3_Othello_AI

#Global variables: 
board=[]
pos_list=[]


#Create board (brand-new board) with initial set-up
def create_board():
    global board
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


# Display_board function
def display_board():
    for row in board:                                                                                
        for col in row:
            print(col,end=' ')      
        print()
                    
def create_pos_list(sym): 
    global pos_list
    pos_list.clear() #Clears previous enteries of this list so it can make new list for new pos
    temp=[]
    if sym=='X':
        oppnt='O'
    else:
        oppnt='X'
    #Range such that only board is considered, outer position numbers are not.
    for r in range(1,9):
        for c in range(1,9):
            if (board[r][c]=='-'):      #Thus, doesn't take positions that are occupied
                any_of_eight=check_eight(r,c,oppnt) #function returns T/F #if even one cell(of eight) is oppnt(opponent),returns true,else false.
                if any_of_eight:
                    temp.append((r,c))
    for loc in temp:
        if check_if_turn(loc[0],loc[1],oppnt,sym):  #function returns T/F #if even one direction (after checking if immediate is oppnt) will lead to turning, returns true, else false.
            pos_list.append(loc)    #Will have the absolute final list of all the possible (all conditions checked) pos for that symbol.
                

# Function: check_eight. 
# check the eight locations with extra condition to prune out and get a smaller list of possibilities. Then every pos checked for turning using check_if_turn function.
def check_eight(r,c,oppnt): 
    if (board[r-1][c]==oppnt) or (board[r-1][c+1]==oppnt) or (board[r][c+1]==oppnt) or (board[r+1][c+1]==oppnt) or (board[r+1][c]==oppnt) or (board[r+1][c-1]==oppnt) or (board[r][c-1]==oppnt) or (board[r-1][c-1]==oppnt): 
        return True   
    else:
        return False


# Function: check_if_turn.
# Algorithm:
# Second level checking of pos_list for if it turns anything:
    #For every location:
       #for all 8 directions, if even one direction returns true, then valid position since turns something (basically,satisfies all conditions).
            #if immediate is player's symbol,skip to the next direction checking.
            #if immediate is opponent's symbol, then:
                 #while next location(in that direction) is opponent's symbol, keep traversing that direction:
                 #has variable 'i', holding that direction's next spot while checking for above point.
                      #if i=='player's symbol':
                          #return true  #this location is allowed and is perfectly valid. 
                      #else:  #anything other than player's symbol    
                          #return false  #Not allowed pos since nothing got turned  
def check_if_turn(r,c,oppnt,sym): 
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
def check_for_moves():  
    if len(pos_list)==0:
        print("Player has no possible moves! Passing the play to other player.")
        print()
        return False
    else:
        return True
           
    
# Function: check_with_pos_list
# Checks if the move is in pos_list, only then it will be a valid move. Else must loop until valid input is given.
def check_with_pos_list(r,c):
    move=(r,c)
    if move in pos_list:
        return True
    else:
        print("Invalid move, please try again.")
        return False
                        
# Function: turn
# Turns the coins for that player's move
def turn_coins(r,c,sym,oppnt):
    global board
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
    print("Turned! Updated board:")
    
                    

# Function: check_endgame
# Algorithm:
# Game ends if:
    # neither players have moves
         # ie create_pos_list for both (use 'and') symbols give empty lists
# Then must check who won (by counting no. of cells for each player and then declare winner with score).
def check_endgame(sym1,sym2):
    create_pos_list(sym1)
    l1=pos_list[:]    #Copying sym1's pos_list to 'l1'
    create_pos_list(sym2)
    l2=pos_list[:]    #Copying sym2's pos_list to 'l2'
    if(len(l1)==0 and len(l2)==0):   #Only if both pos_lists are empty, game over
        print("Players have no more moves! Game over.")
        return 1
    else:
        return 0
        

# Function: check_winner
# Checks who won by counting no. of coins of each player on board and then declares winner (whoever with higher coin count) with their coin counts.
def check_winner(sym1,sym2,P1,P2):
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
        print("Player 2,",P2,"wins!!")
    else:               
        print("Scores:")
        print("Number of Player 1 coins: ",sym1_count)
        print("Number of Player 2 coins: ",sym2_count)
        print("It's a tie!!")
            
    

# Play game
def play():
    print("Let's Play!")
    P1=input("Enter Player 1 name: Black (X): ")
    sym1='X'
    P2=input("Enter Player 2 name: White (O): ")
    sym2='O'
    create_board()    
    # Shows * * * * as if loading
    print("Setting up game")
    for times in range(4):
        for delay in range(10000000):
            if delay==5000000:
                print('*',end='  ')
    #End loading sequence
    print()
    print()
    turn=0
    while(1):
        #Player1
        if turn%2==0:
            create_pos_list(sym1)    
            print("Player 1:",P1,"'s (X) turn:")          
            checking=check_for_moves()
            if checking==True:
                print()
                display_board()
                print()
                while(1):
                    row,column=input("Enter move:(format:row column) ").split()
                    row,column=int(row),int(column)
                    correct=check_with_pos_list(row,column)    
                    if correct:
                            break
                turn_coins(row,column,sym1,sym2)  
                display_board()   #Shows players updated board
                print()
                #Board displayed
                #Move checked and turned
                #Board updated and displayed            

        #Player2
        else:
            create_pos_list(sym2)    
            print("Player 2:",P2,"'s (O) turn:")          
            checking=check_for_moves()
            if checking==True:   
                print()
                display_board()
                print()
                while(1):
                    row,column=input("Enter move:(format:row column) ").split()
                    row,column=int(row),int(column)
                    correct=check_with_pos_list(row,column)    
                    if correct:
                        break
                turn_coins(row,column,sym2,sym1)  
                display_board()   #Shows players updated board
                print()
            #Board displayed
            #Move checked and turned
            #Board updated and displayed
            
        option=int(input("(Press 1 to continue the game and 0 to quit) "))
        print()
        end=check_endgame(sym1,sym2)      
        if (end==1 or option==0):
            check_winner(sym1,sym2,P1,P2)
            print()
            print("Thank you for playing!")
            break
        turn+=1                


        
            

#Main body : MENU 

while(1):
    print()
    print()
    print("                 WELCOME TO THE GAME OTHELLO! ")
    print()
    print("                      Select an option")
    print()
    print("                1.       How to play")
    print("                2. Let's Play : Player VS Player")
    print("                3. Let's Play : Player VS Computer")
    print("                4.         Exit")
    print()
    choice=int(input("Enter your choice: "))
    if choice==1:
        print()
        with open("Othello_instructions.txt") as fp:       
            lines=fp.readlines()
            for i in range(16):
                print(lines[i])
            print()
            a=int(input("Press 1 to read more or 0 to go back to main menu: "))
            if a==1:
                for i in range(16,46):
                    print(lines[i])
                print()
                a=int(input("Press 1 to read more or 0 to go back to main menu: "))
                if a==1:
                    for i in range(46,99):
                        print(lines[i])
                    print()
                    a=input("Enter any key to return to main menu")
    elif choice==2:
        play()
    elif choice==3:
        print()
        SEM3_Othello_AI.play()
    else:
        break   #Exits game
        
            

            
            
