"""
CSCI-404A
Deepak Rajasekhar Karishetti
CSM
"""

#Import the class from file connect4game.py
from connect4game import connect4game
import sys

#One-move game mode:
def one_move_mode(x):

    if x.move_count >= 42:
        print('Gameboard full!\nGAME OVER!')
        sys.exit(0)
    print ('\nGameboard state before move:')

    x.gameboard_screen()
    x.aiPlay()
    print ('Gameboard state after move:')

    x.gameboard_screen()
    x.count_score()

    print('Score:\nPlayer1 = %d\nPlayer2 = %d\n' % (x.p1_score, x.p2_score))
    x.gameboard_file()
    x.gamefile.close()

#Interactive game mode:
def interactive_mode(x, next_player):

    x.gameboard_screen()
    x.count_score()
    print('Score:\nPlayer1 = %d\nPlayer2 = %d\n' % (x.p1_score, x.p2_score))

    if next_player == 'human-next':
        while x.get_move_count() != 42:
            print("Human player turn")
            userMove = int(input("Enter the column number between 1 and 7 where you want to place your move = "))

            if not 0 < userMove < 8:
                print("Column entered invalid, Re-enter column number")
                continue

            if not x.make_move(userMove - 1):
                print("Column = %d is full! Enter different column" % userMove)
                continue

            print("You made a move in column number = " + str(userMove))
            x.gameboard_screen()
            x.gamefile = open("human.txt", 'w')
            x.gameboard_file()
            x.gamefile.close()

            if x.get_move_count() == 42:
                print("Gameboard full!\nGAME OVER!")
                x.count_score()
                print('Score:\nPlayer1 = %d\nPlayer2 = %d\n' % (x.p1_score, x.p2_score))
                break
            else:
                print("Computer is thinking ahead " + str(x.depth) + " steps")
                x.change_move()
                x.aiPlay()
                x.gameboard_screen()
                x.gamefile = open('computer.txt', 'w')
                x.gameboard_file()
                x.gamefile.close()
                x.count_score()

                print('Score:\nPlayer1 = %d\nPlayer2 = %d\n' % (x.p1_score, x.p2_score))
    else:
        x.aiPlay()
        x.gamefile = open('computer.txt', 'w')
        x.gameboard_file()
        x.gamefile.close()
        x.gameboard_screen()
        x.count_score()
        print('Score:\nPlayer1 = %d\nPlayer2 = %d\n' % (x.p1_score, x.p2_score))

        interactive_mode(x, 'human-next')

    if x.get_move_count() == 42:
        if x.p1_score > x.p2_score:
            print("Player1 wins the game!")
        if x.p1_score == x.p2_score:
            print("Game ends in a tie!")
        if x.p1_score < x.p2_score:
            print("Player2 wins the game!")
        print("\nGAME OVER!")

#Calling the main function to implement connect4game:
def main(argv):
    x = connect4game()

    try:
        x.gamefile = open(argv[2], 'r')
        file_lines = x.gamefile.readlines()
        x.gameboard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
        x.current_move = int(file_lines[-1][0])
        x.gamefile.close()

    except:
        print('Input file not found!\nStarting a new game..')

        x.current_move = 1
    x.game_move_check()
    x.depth=argv[4]

    if argv[1] == 'one-move':
        try:
            x.gamefile = open(argv[3], 'w')
        except:
            sys.exit('Output file invalid!')
        one_move_mode(x)
    else:
        interactive_mode(x,argv[3]) 
    
if __name__ == '__main__':
    main(sys.argv)
