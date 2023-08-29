import random
from random import randint
import sys

#Battleship game against AI.

#The board games of the player and the computer:
player_board = []
for x in range(10):
    player_board.append(["."] * 10)  

pc_board=[]
for x in range(10):
    pc_board.append(["."] * 10)

pc_hidden_board=[]
for x in range(10):
    pc_hidden_board.append(["."] * 10)

ship_len=[5,3,3,2,2,2]
five_big_ship=[]
three_big_ship_1=[]
two_big_ship_1=[]

def player_ships (board, five_big_ship, three_big_ship_1, two_big_ship_1, ship_len):
    """create 1x five space big ships, 2x three space big ships, and 3x two space ones. 
    Need to input the orientation and the starting coordinates by chooseing row 0-9 and column 0-9"""
    print_board('player',player_board)
    for len in ship_len:
        while True:
            orientation = input("Enter to orientation of the {} space big ship, H-horizontal or V-vertical: ".format(len)).upper()
            if orientation=='999':
                sys.exit('You chose to quit, Goodbye')
            while orientation not in ('H',"V"):
                print("Enter only 'H' or 'V'")
                orientation = input("Enter to orientation of the {} space big ship, H-horizontal or V-vertical: ".format(len)).upper()
                if orientation=='999':
                    sys.exit('You chose to quit, Goodbye')
            print("Enter the starting coordinates for the {} space big ship".format(len))
            while True:
                try:
                    row=int(input('Ship row 0-9: '))
                    if row==999:
                        sys.exit('You chose to quit, Goodbye') 
                    elif row in (0,1,2,3,4,5,6,7,8,9):
                        break
                    while row not in (0,1,2,3,4,5,6,7,8,9):
                        print('The number is out of range, try again.')
                        row=int(input('Ship row 0-9: '))
                    if row ==int(row):
                        break
                except ValueError:
                    print('That is not a valid number, try again, 0-9.')

            while True:
                try:
                    column=int(input('Ship column 0-9: '))
                    if column==999:
                        sys.exit('You chose to quit, Goodbye') 
                    elif column in (0,1,2,3,4,5,6,7,8,9):
                        break
                    while column not in (0,1,2,3,4,5,6,7,8,9):
                        print('The number is out of range, try again.')
                        column=int(input('Ship column 0-9: '))
                    if column ==int(column):
                        break
                except ValueError:
                    print('That is not a valid number, try again, 0-9.')

            print("Chosen location for the {} space big ship: ({},{},{})".format(len,row,column,orientation))
            if ship_fit(player_board, len, row, column, orientation):
                        
                if ship_overlaps(board, row, column, orientation, len) == False:
                
                    if orientation == "H":
                        for i in range(column, column + len):
                            board[row][i] = "X"
                            if len ==5:
                                a=(row,i)
                                five_big_ship.append(a)
                            elif len == 3:
                                b=(row,i)
                                three_big_ship_1.append(b)
                            elif len == 2:
                                c=(row,i)
                                two_big_ship_1.append(c)

                            if ship_in_board(row+1, i)==True:
                                board[row+1][i] = '-'
                            if ship_in_board(row-1, i)==True:
                                board[row-1][i] = '-'
                            if ship_in_board(row, column-1)==True:
                                board[row][column-1] = '-'
                            if ship_in_board(row, column+len)==True:
                                board[row][column+len] = '-'
                    else:
                        for i in range(row, row + len):
                            board[i][column] = "X"
                            if len ==5:
                                a=(i,column)
                                five_big_ship.append(a)
                            elif len == 3:
                                b=(i,column)
                                three_big_ship_1.append(b)
                            elif len == 2:
                                c=(i,column)
                                two_big_ship_1.append(c)

                            if ship_in_board(row+len, column)==True:
                                board[row+len][column] = '-'
                            if ship_in_board(row-1, column)==True:
                                board[row-1][column] = '-'
                            if ship_in_board(i, column+1)==True:
                                board[i][column+1] = '-'
                            if ship_in_board(i, column-1)==True:
                                board[i][column-1] = '-'
                    print_board('player',player_board)
                    break

    return print_board('player-FINALE',player_board)

five_big_ship_pc=[]
three_big_ship_pc=[]
two_big_ship_pc=[]


def pc_ship(board, five_big_ship_pc, three_big_ship_pc, two_big_ship_pc, ship_len):
    """Function that chooses the ships locations of the computer."""
    for len in ship_len:
        while True:
            orientation=random.choice(['H','V'])
            row, column=randint(0,9), randint(0,9)
            if ship_fit(pc_board, len, row, column, orientation):
                        
                if ship_overlaps(board, row, column, orientation, len) == False:
                
                    if orientation == "H":
                        for i in range(column, column + len):
                            board[row][i] = "X"
                            if len ==5:
                                a=(row,i)
                                five_big_ship_pc.append(a)
                            elif len == 3:
                                b=(row,i)
                                three_big_ship_pc.append(b)
                            elif len == 2:
                                c=(row,i)
                                two_big_ship_pc.append(c)
                            
                            if ship_in_board(row+1, i)==True:
                                board[row+1][i] = '-'
                            if ship_in_board(row-1, i)==True:
                                board[row-1][i] = '-'
                            if ship_in_board(row, column-1)==True:
                                board[row][column-1] = '-'
                            if ship_in_board(row, column+len)==True:
                                board[row][column+len] = '-'
                    else:
                        for i in range(row, row + len):
                            board[i][column] = "X"
                            if len ==5:
                                a=(i,column)
                                five_big_ship_pc.append(a)
                            elif len == 3:
                                b=(i,column)
                                three_big_ship_pc.append(b)
                            elif len == 2:
                                c=(i,column)
                                two_big_ship_pc.append(c)

                            if ship_in_board(row+len, column)==True:
                                board[row+len][column] = '-'
                            if ship_in_board(row-1, column)==True:
                                board[row-1][column] = '-'
                            if ship_in_board(i, column+1)==True:
                                board[i][column+1] = '-'
                            if ship_in_board(i, column-1)==True:
                                board[i][column-1] = '-'
                    break

    return print_board('computer',pc_hidden_board)


def ship_fit(board, len, row, column, orientation):
    """Check if the length of the ship fitts the game board according to the location chosen."""
    if orientation == "H":
        if column + len > 10:
            if board==player_board:
                print("The ship is out of the board game.")
                return False
            else:
                return False
        else:
            return True
    else:
        if row + len > 10:
            if board==player_board:
                print("The ship is out of the board game.")
                return False
            else:
                return False
        else:
            return True


def ship_in_board(row, column):
    """Check if the number of the row or the column is out of the board game."""
    if row > 9:
        return False
    elif row < 0:
        return False
    elif column > 9:
        return False
    elif column < 0:
        return False
    else:
        return True


def ship_outline(board, row, column):
    """Helps the AI no to guess location which is too close to other, already hit, ship, since according to the rules there must be at least 
    one free space between ships."""
    if ship_in_board(row+1, column)==True:
        if board[row+1][column] == "0":
            return True
    if ship_in_board(row-1, column)==True:
        if board[row-1][column] == "0":
            return True
    if ship_in_board(row, column+1)==True:
        if board[row][column+1] == "0":
            return True
    if ship_in_board(row, column-1)==True:
        if board[row][column-1] == "0":
            return True


def ship_overlaps(board, row, column, orientation, len):
    """Check if ships are not being placed one over the other."""
    if orientation == "H":
        for i in range(column, column + len):
            if board[row][i] == "X":
                if board==player_board:
                    print("The ship overlapping another ship.")
                    return True
                else:
                    return True
            elif board[row][i] == "-":
                if board==player_board:
                    print("The ship is too close to another ship.")
                    return True
                else:
                    return True
    else:
        for i in range(row, row + len):
            if board[i][column] == "X":
                if board==player_board:
                    print("The ship is overlapping another ship")
                    return True
                else:
                    return True
            elif board[i][column] == "-":
                if board==player_board:
                    print("The ship is too close to another ship")
                    return True
                else:
                    return True
    return False


def print_board(name,board):
    print('The board game of the {}'.format(name))
    print('  0 1 2 3 4 5 6 7 8 9 ')
    row_number=0
    for row in board:
        print(row_number,(" ").join(row))
        row_number+=1
    return ''


def player_guess(pc_board, pc_hidden_board): 
    """The guess of the player for the location of the computer's ships."""
    while True:
                try:
                    row=int(input('Enter your guess of the ship row 0-9: '))
                    if row==999:
                       sys.exit('You chose to quit, Goodbye') 
                    elif row in (0,1,2,3,4,5,6,7,8,9):
                        break
                    while row not in (0,1,2,3,4,5,6,7,8,9):
                        print('The number is out of range, try again.')
                        row=int(input('Enter your guess of the ship row 0-9: '))
                    if row ==int(row):
                        break
                except ValueError:
                    print('That is not a valid number, try again, 0-9.')

    while True:
        try:
            column=int(input('Enter your guess of the ship column 0-9: '))
            if column==999:
                sys.exit('You chose to quit, Goodbye') 
            elif column in (0,1,2,3,4,5,6,7,8,9):
                break
            while column not in (0,1,2,3,4,5,6,7,8,9):
                print('The number is out of range, try again.')
                column=int(input('Enter your guess of the ship column 0-9: '))
            if column ==int(column):
                break
        except ValueError:
            print('That is not a valid number, try again, 0-9.')
    
    while pc_board[row][column]=='~' or pc_board[row][column]=='0':
        print ('You already chose that location, try again.' )
        while True:
                try:
                    row=int(input('Enter your guess of the ship row 0-9: '))
                    if row==999:
                       sys.exit('You chose to quit, Goodbye') 
                    elif row in (0,1,2,3,4,5,6,7,8,9):
                        break
                    while row not in (0,1,2,3,4,5,6,7,8,9):
                        print('The number is out of range, try again')
                        row=int(input('Enter your guess of the ship row 0-9: '))
                    if row ==int(row):
                        break
                except ValueError:
                    print('That is not a valid number, try again, 0-9.')

        while True:
            try:
                column=int(input('Enter your guess of the ship column 0-9: '))
                if column==999:
                    sys.exit('You chose to quit, Goodbye') 
                elif column in (0,1,2,3,4,5,6,7,8,9):
                    break
                while column not in (0,1,2,3,4,5,6,7,8,9):
                    print('The number is out of range, try again')
                    column=int(input('Enter your guess of the ship column 0-9: '))
                if column ==int(column):
                    break
            except ValueError:
                print('That is not a valid number, try again, 0-9.')
    
    print("Chosen location for coumputer's ship: ({},{})".format(row,column))

    if pc_board[row][column]=='X':
        print("WOW! It's a hit!")
        pc_board[row][column]='0'
        pc_hidden_board[row][column]='0'
        #a=(row,column)
        if (row, column) in five_big_ship_pc:
            print("You hit a aircraft carrier (5 squares big ship)")
        elif (row, column) in three_big_ship_pc:
            print("You hit a battleship (3 squares big ship)")
        elif (row, column) in two_big_ship_pc:
            print("You hit a submarine (2 squares big ship)")
        
        return print_board("computer", pc_hidden_board)
    
    elif pc_board[row][column]=='.' or pc_board[row][column]=='-': 
        print("You missed, maybe next time...")
        pc_board[row][column]='~'
        pc_hidden_board[row][column]='~'
    
        return print_board("computer", pc_hidden_board)

targets=[]
more_targets=[]
four_ship=[]
five_ship=[]
end_targets=[]


def pc_guess(player_board):
    """The guess of the computer."""
    if next_target(player_board, more_targets)== False:
        if next_target(player_board, four_ship)==False:
            if next_target(player_board, five_ship)==False:
                if next_target(player_board, end_targets)==False:
                    if finder(player_board) == False:
                        row, column=randint(0,9), randint(0,9)
                        while ship_outline(player_board, row, column)==True or player_board[row][column]=='~' or player_board[row][column]=='0':
                            row, column=randint(0,9), randint(0,9)
                        print("Computer's guess: ({},{})".format(row,column))

                        if player_board[row][column]=='X':
                            print("Oh no... computer hit one of your ships.")
                            player_board[row][column]='0'
                            targets.append(row)
                            targets.append(column)
                        elif player_board[row][column]=='.' or player_board[row][column]=='-':
                            print("You are lucky, computer missed.")
                            player_board[row][column]='~'
   
    return print_board("player", player_board)


def finder(player_board): 
    """If first guess of the computer was a hit, it will try the sink the entire ship. This function collects the next targets."""
    if len(targets) !=0:
        row=targets[0]
        column=targets[1]
        potential_targets = [(row + 1, column), (row, column + 1),
                        (row - 1, column), (row, column - 1)]
        next_row, next_column=random.choice(potential_targets)
        while ship_in_board(next_row, next_column)==False or player_board[next_row][next_column]=='~' or player_board[next_row][next_column]=='0':
            next_row, next_column=random.choice(potential_targets)
        print("Computer's guess: ({},{})".format(next_row,next_column))       
        if player_board[next_row][next_column]=='.' or player_board[next_row][next_column]=='-': 
                print("You are lucky, computer missed.")
                player_board[next_row][next_column]='~'
        elif player_board[next_row][next_column]=='X':
            print("Oh no... computer hit one of your ships.")
            player_board[next_row][next_column]='0'
            next_move=(next_row, next_column)

            if (row,column) in five_big_ship:
                if next_move==(row + 1, column): 
                    if ship_in_board(row+2, column)==True:
                        more_targets.append(row+2)
                        more_targets.append(column)
                        if player_board[row+2][column]=='X':
                            if ship_in_board(row+3, column)==True:
                                four_ship.append(row+3)
                                four_ship.append(column)
                                if player_board[row+3][column]=='X':
                                    if ship_in_board(row+4, column)==True:
                                        five_ship.append(row+4)
                                        five_ship.append(column)
                                        if player_board[row+4][column]=='.' or player_board[row+4][column]=='-' or player_board[row+4][column]=='~':
                                            if ship_in_board(row-1, column)==True:
                                                end_targets.append(row-1)
                                                end_targets.append(column)
                                    else:
                                        if ship_in_board(row-1, column)==True:
                                                end_targets.append(row-1)
                                                end_targets.append(column)
                                elif player_board[row+3][column]=='.' or player_board[row+3][column]=='-':
                                    if ship_in_board(row-1, column)==True:
                                        five_ship.append(row-1)
                                        five_ship.append(column)
                                        if player_board[row-1][column]=='X':
                                            if ship_in_board(row-2, column)==True:
                                                end_targets.append(row-2)
                                                end_targets.append(column)
                                elif player_board[row+3][column]=='~':
                                    four_ship.pop(1)
                                    four_ship.pop(0)
                                    if ship_in_board(row-1, column)==True:
                                        four_ship.append(row-1)
                                        four_ship.append(column)
                                        if player_board[row-1][column]=='X':
                                            if ship_in_board(row-2, column)==True:
                                                five_ship.append(row-2)
                                                five_ship.append(column)
                            else:
                                if ship_in_board(row-1, column)==True:
                                        four_ship.append(row-1)
                                        four_ship.append(column)
                                        if player_board[row-1][column]=='X':
                                            if ship_in_board(row-2, column)==True:
                                                five_ship.append(row-2)
                                                five_ship.append(column)
                        elif player_board[row+2][column]=='.' or player_board[row+2][column]=='-':
                            if ship_in_board(row-1, column)==True:
                                four_ship.append(row-1)
                                four_ship.append(column)
                                if player_board[row-1][column]=='X':
                                    if ship_in_board(row-2, column)==True:
                                        five_ship.append(row-2)
                                        five_ship.append(column)
                                        if player_board[row-2][column]=='X': 
                                            if ship_in_board(row-3, column)==True:
                                                end_targets.append(row-3)
                                                end_targets.append(column)
                        elif player_board[row+2][column]=='~': 
                            more_targets.pop(1)
                            more_targets.pop(0)
                            if ship_in_board(row-1, column)==True:
                                more_targets.append(row-1)
                                more_targets.append(column)
                                if player_board[row-1][column]=='X':
                                    if ship_in_board(row-2, column)==True:
                                        four_ship.append(row-2)
                                        four_ship.append(column)
                                        if player_board[row-2][column]=='X':
                                            if ship_in_board(row-3, column)==True:
                                                five_ship.append(row-3)
                                                five_ship.append(column)
                    elif ship_in_board(row+2, column)==False:
                        more_targets.append(row-1)
                        more_targets.append(column)
                        if player_board[row-1][column]=='X':
                            if ship_in_board(row-2, column)==True:
                                four_ship.append(row-2)
                                four_ship.append(column)
                                if player_board[row-2][column]=='X':
                                    if ship_in_board(row-3, column)==True:
                                        five_ship.append(row-3)
                                        five_ship.append(column)
                elif next_move==(row, column+1):
                    if ship_in_board(row, column+2)==True:
                        more_targets.append(row)
                        more_targets.append(column+2)
                        if player_board[row][column+2]=='X':
                            if ship_in_board(row, column+3)==True:
                                four_ship.append(row)
                                four_ship.append(column+3)
                                if player_board[row][column+3]=='X':
                                    if ship_in_board(row, column+4)==True:
                                        five_ship.append(row)
                                        five_ship.append(column+4)
                                        if player_board[row][column+4]=='.' or player_board[row][column+4]=='-' or player_board[row][column+4]=='~':
                                            if ship_in_board(row, column-1)==True:
                                                end_targets.append(row)
                                                end_targets.append(column-1)
                                    else:
                                        if ship_in_board(row, column-1)==True:
                                                end_targets.append(row)
                                                end_targets.append(column-1)
                                elif player_board[row][column+3]=='.' or player_board[row][column+3]=='-':
                                    if ship_in_board(row, column-1)==True:
                                        five_ship.append(row)
                                        five_ship.append(column-1)
                                        if player_board[row][column-1]=='X':
                                            if ship_in_board(row, column-2)==True:
                                                end_targets.append(row)
                                                end_targets.append(column-2)
                                elif player_board[row][column+3]=='~':
                                    four_ship.pop(1)
                                    four_ship.pop(0)
                                    if ship_in_board(row, column-1)==True:
                                        four_ship.append(row)
                                        four_ship.append(column-1)
                                        if player_board[row][column-1]=='X':
                                            if ship_in_board(row, column-2)==True:
                                                five_ship.append(row)
                                                five_ship.append(column-2)
                            else:
                                if ship_in_board(row, column-1)==True:
                                        four_ship.append(row)
                                        four_ship.append(column-1)
                                        if player_board[row][column-1]=='X':
                                            if ship_in_board(row, column-2)==True:
                                                five_ship.append(row)
                                                five_ship.append(column-2)
                                                if player_board[row][column-2]=='X':
                                                    if ship_in_board(row, column-3)==True:
                                                        end_targets.append(row)
                                                        end_targets.append(column-3)
                        elif player_board[row][column+2]=='.' or player_board[row][column+2]=='-':
                            if ship_in_board(row, column-1)==True:
                                four_ship.append(row)
                                four_ship.append(column-1)
                                if player_board[row][column-1]=='X':
                                    if ship_in_board(row, column-2)==True:
                                        five_ship.append(row)
                                        five_ship.append(column-2)
                                        if player_board[row][column-2]=='X':
                                            if ship_in_board(row, column-3)==True:
                                                end_targets.append(row)
                                                end_targets.append(column-3)
                        elif player_board[row][column+2]=='~':
                            more_targets.pop(1)
                            more_targets.pop(0)
                            if ship_in_board(row, column-1)==True:
                                more_targets.append(row)
                                more_targets.append(column-1)
                                if player_board[row][column-1]=='X':
                                    if ship_in_board(row, column-2)==True:
                                        four_ship.append(row)
                                        four_ship.append(column-2)
                                        if player_board[row][column-2]=='X':
                                            if ship_in_board(row, column-3)==True:
                                                five_ship.append(row)
                                                five_ship.append(column-3)
                    elif ship_in_board(row, column+2)==False:
                        more_targets.append(row)
                        more_targets.append(column-1)
                        if player_board[row][column-1]=='X':
                            if ship_in_board(row, column-2)==True:
                                four_ship.append(row)
                                four_ship.append(column-2)
                                if player_board[row][column-2]=='X':
                                    if ship_in_board(row, column-3)==True:
                                        five_ship.append(row)
                                        five_ship.append(column-3)
                elif next_move==(row, column-1):
                    if ship_in_board(row, column-2)==True:
                        more_targets.append(row)
                        more_targets.append(column-2)
                        if player_board[row][column-2]=='X':
                            if ship_in_board(row, column-3)==True:
                                four_ship.append(row)
                                four_ship.append(column-3)
                                if player_board[row][column-3]=='X':
                                    if ship_in_board(row, column-4)==True:
                                        five_ship.append(row)
                                        five_ship.append(column-4)
                                        if player_board[row][column-4]=='.' or player_board[row][column-4]=='-' or player_board[row][column-4]=='~':
                                            if ship_in_board(row, column+1)==True:
                                                end_targets.append(row)
                                                end_targets.append(column+1)
                                    else:
                                        if ship_in_board(row, column+1)==True:
                                            end_targets.append(row)
                                            end_targets.append(column+1)  
                                elif player_board[row][column-3]=='.' or player_board[row][column-3]=='-':
                                    if ship_in_board(row, column+1)==True:
                                        five_ship.append(row)
                                        five_ship.append(column+1)
                                        if player_board[row][column+1]=='X':
                                            if ship_in_board(row, column+2)==True:
                                                end_targets.append(row)
                                                end_targets.append(column+2)
                                elif player_board[row][column-3]=='~':
                                    four_ship.pop(1)
                                    four_ship.pop(0)
                                    if ship_in_board(row, column+1)==True:
                                        four_ship.append(row)
                                        four_ship.append(column+1)
                                        if player_board[row][column+1]=='X':
                                            if ship_in_board(row, column+2)==True:
                                                five_ship.append(row)
                                                five_ship.append(column+2)
                            else:
                                if ship_in_board(row, column+1)==True:
                                        four_ship.append(row)
                                        four_ship.append(column+1)
                                        if player_board[row][column+1]=='X':
                                            if ship_in_board(row, column+2)==True:
                                                five_ship.append(row)
                                                five_ship.append(column+2)
                        elif player_board[row][column-2]=='.' or player_board[row][column-2]=='-':
                            if ship_in_board(row, column+1)==True:
                                four_ship.append(row)
                                four_ship.append(column+1)
                                if player_board[row][column+1]=='X':
                                    if ship_in_board(row, column+2)==True:
                                        five_ship.append(row)
                                        five_ship.append(column+2)
                                        if player_board[row][column+2]=='X':
                                            if ship_in_board(row, column+3)==True:
                                                end_targets.append(row)
                                                end_targets.append(column+3)
                        elif player_board[row][column-2]=='~':
                            more_targets.pop(1)
                            more_targets.pop(0)
                            if ship_in_board(row, column+1)==True:
                                more_targets.append(row)
                                more_targets.append(column+1)
                                if player_board[row][column+1]=='X':
                                    if ship_in_board(row, column+2)==True:
                                        four_ship.append(row)
                                        four_ship.append(column+2)
                                        if player_board[row][column+2]=='X':
                                            if ship_in_board(row, column+3)==True:
                                                five_ship.append(row)
                                                five_ship.append(column+3)
                    elif ship_in_board(row, column-2)==False:
                        more_targets.append(row)
                        more_targets.append(column+1)
                        if player_board[row][column+1]=='X':
                            if ship_in_board(row, column+2)==True:
                                four_ship.append(row)
                                four_ship.append(column+2)
                                if player_board[row][column+2]=='X':
                                    if ship_in_board(row, column+3)==True:
                                        five_ship.append(row)
                                        five_ship.append(column+3)
                elif next_move==(row-1, column):
                    if ship_in_board(row-2, column)==True:
                        more_targets.append(row-2)
                        more_targets.append(column)
                        if player_board[row-2][column]=='X':
                            if ship_in_board(row-3, column)==True:
                                four_ship.append(row-3)
                                four_ship.append(column)
                                if player_board[row-3][column]=='X':
                                    if ship_in_board(row-4, column)==True:
                                        five_ship.append(row-4)
                                        five_ship.append(column)
                                        if player_board[row-4][column]=='.' or player_board[row-4][column]=='-' or player_board[row-4][column]=='~':
                                            if ship_in_board(row+1, column)==True:
                                                end_targets.append(row+1)
                                                end_targets.append(column)
                                    else:
                                        if ship_in_board(row+1, column)==True:
                                                end_targets.append(row+1)
                                                end_targets.append(column)
                                elif player_board[row-3][column]=='.' or player_board[row-3][column]=='-' or player_board[row-3][column]=='~':
                                    if ship_in_board(row+1, column)==True:
                                        five_ship.append(row+1)
                                        five_ship.append(column)
                                        if player_board[row+1][column]=='X':
                                            if ship_in_board(row+2, column)==True:
                                                end_targets.append(row+2)
                                                end_targets.append(column)
                                elif player_board[row-3][column]=='~':
                                    four_ship.pop(1)
                                    four_ship.pop(0)
                                    if ship_in_board(row+1, column)==True:
                                        four_ship.append(row+1)
                                        four_ship.append(column)
                                        if player_board[row+1][column]=='X':
                                            if ship_in_board(row+2, column)==True:
                                                five_ship.append(row+2)
                                                five_ship.append(column)
                            else:
                                if ship_in_board(row+1, column)==True:
                                        four_ship.append(row+1)
                                        four_ship.append(column)
                                        if player_board[row+1][column]=='X':
                                            if ship_in_board(row+2, column)==True:
                                                five_ship.append(row+2)
                                                five_ship.append(column)
                        elif player_board[row-2][column]=='.' or player_board[row-2][column]=='-':
                            if ship_in_board(row+1, column)==True:
                                four_ship.append(row+1)
                                four_ship.append(column)
                                if player_board[row+1][column]=='X':
                                    if ship_in_board(row+2, column)==True:
                                        five_ship.append(row+2)
                                        five_ship.append(column)
                                        if player_board[row+2][column]=='X':
                                            if ship_in_board(row+3, column)==True:
                                                end_targets.append(row+3)
                                                end_targets.append(column)
                        elif player_board[row-2][column]=='~':
                            more_targets.pop(1)
                            more_targets.pop(0)
                            if ship_in_board(row+1, column)==True:
                                more_targets.append(row+1)
                                more_targets.append(column)
                                if player_board[row+1][column]=='X':
                                    if ship_in_board(row+2, column)==True:
                                        four_ship.append(row+2)
                                        four_ship.append(column)
                                        if player_board[row+2][column]=='X':
                                            if ship_in_board(row+3, column)==True:
                                                five_ship.append(row+3)
                                                five_ship.append(column)
                    elif ship_in_board(row-2, column)==False:
                        more_targets.append(row+1)
                        more_targets.append(column)
                        if player_board[row+1][column]=='X':
                            if ship_in_board(row+2, column)==True:
                                four_ship.append(row+2)
                                four_ship.append(column)
                                if player_board[row+2][column]=='X':
                                    if ship_in_board(row+3, column)==True:
                                        five_ship.append(row+3)
                                        five_ship.append(column)
            elif (row,column) in three_big_ship_1:
                if next_move==(row + 1, column): 
                    if ship_in_board(row+2, column)==True:
                        more_targets.append(row+2)
                        more_targets.append(column)
                        if player_board[row+2][column]=='.' or player_board[row+2][column]=='-':
                            if ship_in_board(row-1, column)==True:
                                four_ship.append(row-1)
                                four_ship.append(column)
                        elif player_board[row+2][column]=='~': 
                            more_targets.pop(1)
                            more_targets.pop(0)
                            if ship_in_board(row-1, column)==True:
                                more_targets.append(row-1)
                                more_targets.append(column)
                    elif ship_in_board(row+2, column)==False:
                        more_targets.append(row-1)
                        more_targets.append(column)
                elif next_move==(row, column+1):
                    if ship_in_board(row, column+2)==True:
                        more_targets.append(row)
                        more_targets.append(column+2)
                        if player_board[row][column+2]=='.' or player_board[row][column+2]=='-':
                            if ship_in_board(row, column-1)==True:
                                four_ship.append(row)
                                four_ship.append(column-1)
                        elif player_board[row][column+2]=='~':
                            more_targets.pop(1)
                            more_targets.pop(0)
                            if ship_in_board(row, column-1)==True:
                                more_targets.append(row)
                                more_targets.append(column-1)
                    elif ship_in_board(row, column+2)==False:
                        more_targets.append(row)
                        more_targets.append(column-1)
                elif next_move==(row, column-1):
                    if ship_in_board(row, column-2)==True:
                        more_targets.append(row)
                        more_targets.append(column-2)
                        if player_board[row][column-2]=='.' or player_board[row][column-2]=='-':
                            if ship_in_board(row, column+1)==True:
                                four_ship.append(row)
                                four_ship.append(column+1)
                        elif player_board[row][column-2]=='~':
                            more_targets.pop(1)
                            more_targets.pop(0)
                            if ship_in_board(row, column+1)==True:
                                more_targets.append(row)
                                more_targets.append(column+1)
                    elif ship_in_board(row, column-2)==False:
                        more_targets.append(row)
                        more_targets.append(column+1)
                elif next_move==(row-1, column):
                    if ship_in_board(row-2, column)==True:
                        more_targets.append(row-2)
                        more_targets.append(column)
                        if player_board[row-2][column]=='.' or player_board[row-2][column]=='-':
                            if ship_in_board(row+1, column)==True:
                                four_ship.append(row+1)
                                four_ship.append(column)
                        elif player_board[row-2][column]=='~':
                            more_targets.pop(1)
                            more_targets.pop(0)
                            if ship_in_board(row+1, column)==True:
                                more_targets.append(row+1)
                                more_targets.append(column)
                    elif ship_in_board(row-2, column)==False:
                        more_targets.append(row+1)
                        more_targets.append(column)
            targets.pop(1)
            targets.pop(0)
                    
    else:
        return False
    

def next_target(player_board, target_list):
    """Function to execute the next targets gathered in def finder()."""
    if len(target_list) !=0:
        row=target_list[0]
        column=target_list[1]
        if ship_in_board(row, column)==True:
            print("Computer's guess: ({},{})".format(row,column))
            if player_board[row][column]=='.' or player_board[row][column]=='-':
                print("You are lucky, computer missed.")
                player_board[row][column]='~'
                target_list.pop(1)
                target_list.pop(0)
                    
            elif player_board[row][column]=='X':
                print("Oh no... computer hit one of your ships.")
                player_board[row][column]='0'
                target_list.pop(1)
                target_list.pop(0)
        else:
            target_list.pop(1)
            target_list.pop(0)
    else: 
        return False


def count_hits(board):
    """counts the hits in each borad game until all the ships are sunk and the game is over."""
    count=0
    for row in board:
        for column in row:
            if column=='0':
                count+=1
    return count


print("Welcome to Battleship Game")
print("Battleship is a strategy type guessing game played by you as the player and the computer.") 
print("It is played on a 10x10 board, divided into squares identified by numbers from 0 to 9.")
print("Each opponent has its own board on which six ships should be placed:")
print("one aircraft carrier- 5 squares big ship, two battleships- 3 squares big ship and three submarines- 2 squares big ship. ")
print("In order to place a ship you should first choose its orientation: horizontal or vertical,")
print("then choose the starting coordinates by entering a row number and a column number.")
print("Ships are not allowed to touch each other horizontally or vertically (diagonally is ok),")
print("you should leave at least one square free between ships.")
print("After all the ships have been positioned on the board the game begins.")
print("In each round, each player guesses a location of a ship by choosing a row and a column.")
print("If a ship was hit you will know its size. ")
print("The first player to hit all of the opponent’s fleet wins the game, and the game is over.")
print("You can choose to quit the game at any point by entering ‘999’.")
print("GOOD LUCK!")
print("‘.’ - clear board square")
print("‘X’ - square occupied by a ship")
print("‘O’ - ship that was hit")
print("‘~’ - missed hit")
print("‘-‘ - square on which you are not allowed to place a ship")

print(player_ships (player_board, five_big_ship, three_big_ship_1, two_big_ship_1, ship_len))
pc_ship(pc_board, five_big_ship_pc, three_big_ship_pc, two_big_ship_pc, ship_len)

while True:
    print(player_guess(pc_board, pc_hidden_board))
    print(pc_guess(player_board))
    if  count_hits(pc_board) == 17:
        print("Congratulations! you have sunk all of the computer's fleet! YOU WIN")
        break
    elif count_hits(player_board) == 17:
        print("Unfortunatly all of your fleet has been destroyed. YOU LOOSE")
        break
print("GAME OVER.")


            