#!/usr/bin/env python

import copy
import random
import sys

#Defining the req empty dictionary and list:
utility_val = dict()
score_list = list()
infinity = float('inf')

#Defining a class:
class connect4game:
    def __init__(self):
        self.gameboard = [[0 for i in range(7)] for j in range(6)]
        self.current_move = 0
        self.move_count = 0
        self.p1_score = 0
        self.p2_score = 0
        self.gamefile = None

        self.depth = 1

    #Calculate number of moves:
    def game_move_check(self):
        self.move_count = sum(1 for i in self.gameboard for j in i if j)
    
    #Return the value of number of moves:
    def get_move_count(self):
        return sum(1 for i in self.gameboard for j in i if j)

    #Print to terminal:
    def gameboard_screen(self):
        print(' ---------------')
        for i in range(6):
            print('|'),
            for j in range(7):
                print('{}'.format(int(self.gameboard[i][j]))),
            print('|')
        print(' ---------------')

    #Print to file:
    def gameboard_file(self):
        for row in self.gameboard:
            self.gamefile.write(''.join(str(col) for col in row) + '\r')
        self.gamefile.write('{}\r'.format(str(self.current_move)))

    #AI playing moves:
    def aiPlay(self):
        random_column = self.minimax(int(self.depth))
        result = self.make_move(random_column)
        if not result:
            print('No Result')
        else:
            print('Player = %d\nColumn = %d\n' % (self.current_move, random_column + 1))
            self.change_move()

    #Place move in the input column number:
    def make_move(self, column):
        if not self.gameboard[0][column]:
            for i in range(5, -1, -1):
                if not self.gameboard[i][column]:
                    self.gameboard[i][column] = self.current_move
                    self.move_count += 1
                    return 1
    #Check moves:
    def check_piece(self, column, opp):
        if not self.gameboard[0][column]:
            for i in range(5, -1, -1):
                if not self.gameboard[i][column]:
                    self.gameboard[i][column] = opp
                    self.move_count += 1
                    return 1

    #Count scores of players:
    def count_score(self):
        self.p1_score = 0;
        self.p2_score = 0;

        # Check horizontally
        for row in self.gameboard:

            # Check player 1
            if row[0:4] == [1] * 4:
                self.p1_score += 1
            if row[1:5] == [1] * 4:
                self.p1_score += 1
            if row[2:6] == [1] * 4:
                self.p1_score += 1
            if row[3:7] == [1] * 4:
                self.p1_score += 1
            # Check player 2
            if row[0:4] == [2] * 4:
                self.p2_score += 1
            if row[1:5] == [2] * 4:
                self.p2_score += 1
            if row[2:6] == [2] * 4:
                self.p2_score += 1
            if row[3:7] == [2] * 4:
                self.p2_score += 1

        # Check vertically
        for j in range(7):

            # Check player 1
            if (self.gameboard[0][j] == 1 and self.gameboard[1][j] == 1 and
                    self.gameboard[2][j] == 1 and self.gameboard[3][j] == 1):
                self.p1_score += 1
            if (self.gameboard[1][j] == 1 and self.gameboard[2][j] == 1 and
                    self.gameboard[3][j] == 1 and self.gameboard[4][j] == 1):
                self.p1_score += 1
            if (self.gameboard[2][j] == 1 and self.gameboard[3][j] == 1 and
                    self.gameboard[4][j] == 1 and self.gameboard[5][j] == 1):
                self.p1_score += 1

            # Check player 2
            if (self.gameboard[0][j] == 2 and self.gameboard[1][j] == 2 and
                    self.gameboard[2][j] == 2 and self.gameboard[3][j] == 2):
                self.p2_score += 1
            if (self.gameboard[1][j] == 2 and self.gameboard[2][j] == 2 and
                    self.gameboard[3][j] == 2 and self.gameboard[4][j] == 2):
                self.p2_score += 1
            if (self.gameboard[2][j] == 2 and self.gameboard[3][j] == 2 and
                    self.gameboard[4][j] == 2 and self.gameboard[5][j] == 2):
                self.p2_score += 1

        # Check diagonally

        # Check player 1
        if (self.gameboard[2][0] == 1 and self.gameboard[3][1] == 1 and
                self.gameboard[4][2] == 1 and self.gameboard[5][3] == 1):
            self.p1_score += 1
        if (self.gameboard[1][0] == 1 and self.gameboard[2][1] == 1 and
                self.gameboard[3][2] == 1 and self.gameboard[4][3] == 1):
            self.p1_score += 1
        if (self.gameboard[2][1] == 1 and self.gameboard[3][2] == 1 and
                self.gameboard[4][3] == 1 and self.gameboard[5][4] == 1):
            self.p1_score += 1
        if (self.gameboard[0][0] == 1 and self.gameboard[1][1] == 1 and
                self.gameboard[2][2] == 1 and self.gameboard[3][3] == 1):
            self.p1_score += 1
        if (self.gameboard[1][1] == 1 and self.gameboard[2][2] == 1 and
                self.gameboard[3][3] == 1 and self.gameboard[4][4] == 1):
            self.p1_score += 1
        if (self.gameboard[2][2] == 1 and self.gameboard[3][3] == 1 and
                self.gameboard[4][4] == 1 and self.gameboard[5][5] == 1):
            self.p1_score += 1
        if (self.gameboard[0][1] == 1 and self.gameboard[1][2] == 1 and
                self.gameboard[2][3] == 1 and self.gameboard[3][4] == 1):
            self.p1_score += 1
        if (self.gameboard[1][2] == 1 and self.gameboard[2][3] == 1 and
                self.gameboard[3][4] == 1 and self.gameboard[4][5] == 1):
            self.p1_score += 1
        if (self.gameboard[2][3] == 1 and self.gameboard[3][4] == 1 and
                self.gameboard[4][5] == 1 and self.gameboard[5][6] == 1):
            self.p1_score += 1
        if (self.gameboard[0][2] == 1 and self.gameboard[1][3] == 1 and
                self.gameboard[2][4] == 1 and self.gameboard[3][5] == 1):
            self.p1_score += 1
        if (self.gameboard[1][3] == 1 and self.gameboard[2][4] == 1 and
                self.gameboard[3][5] == 1 and self.gameboard[4][6] == 1):
            self.p1_score += 1
        if (self.gameboard[0][3] == 1 and self.gameboard[1][4] == 1 and
                self.gameboard[2][5] == 1 and self.gameboard[3][6] == 1):
            self.p1_score += 1

        if (self.gameboard[0][3] == 1 and self.gameboard[1][2] == 1 and
                self.gameboard[2][1] == 1 and self.gameboard[3][0] == 1):
            self.p1_score += 1
        if (self.gameboard[0][4] == 1 and self.gameboard[1][3] == 1 and
                self.gameboard[2][2] == 1 and self.gameboard[3][1] == 1):
            self.p1_score += 1
        if (self.gameboard[1][3] == 1 and self.gameboard[2][2] == 1 and
                self.gameboard[3][1] == 1 and self.gameboard[4][0] == 1):
            self.p1_score += 1
        if (self.gameboard[0][5] == 1 and self.gameboard[1][4] == 1 and
                self.gameboard[2][3] == 1 and self.gameboard[3][2] == 1):
            self.p1_score += 1
        if (self.gameboard[1][4] == 1 and self.gameboard[2][3] == 1 and
                self.gameboard[3][2] == 1 and self.gameboard[4][1] == 1):
            self.p1_score += 1
        if (self.gameboard[2][3] == 1 and self.gameboard[3][2] == 1 and
                self.gameboard[4][1] == 1 and self.gameboard[5][0] == 1):
            self.p1_score += 1
        if (self.gameboard[0][6] == 1 and self.gameboard[1][5] == 1 and
                self.gameboard[2][4] == 1 and self.gameboard[3][3] == 1):
            self.p1_score += 1
        if (self.gameboard[1][5] == 1 and self.gameboard[2][4] == 1 and
                self.gameboard[3][3] == 1 and self.gameboard[4][2] == 1):
            self.p1_score += 1
        if (self.gameboard[2][4] == 1 and self.gameboard[3][3] == 1 and
                self.gameboard[4][2] == 1 and self.gameboard[5][1] == 1):
            self.p1_score += 1
        if (self.gameboard[1][6] == 1 and self.gameboard[2][5] == 1 and
                self.gameboard[3][4] == 1 and self.gameboard[4][3] == 1):
            self.p1_score += 1
        if (self.gameboard[2][5] == 1 and self.gameboard[3][4] == 1 and
                self.gameboard[4][3] == 1 and self.gameboard[5][2] == 1):
            self.p1_score += 1
        if (self.gameboard[2][6] == 1 and self.gameboard[3][5] == 1 and
                self.gameboard[4][4] == 1 and self.gameboard[5][3] == 1):
            self.p1_score += 1

        # Check player 2
        if (self.gameboard[2][0] == 2 and self.gameboard[3][1] == 2 and
                self.gameboard[4][2] == 2 and self.gameboard[5][3] == 2):
            self.p2_score += 1
        if (self.gameboard[1][0] == 2 and self.gameboard[2][1] == 2 and
                self.gameboard[3][2] == 2 and self.gameboard[4][3] == 2):
            self.p2_score += 1
        if (self.gameboard[2][1] == 2 and self.gameboard[3][2] == 2 and
                self.gameboard[4][3] == 2 and self.gameboard[5][4] == 2):
            self.p2_score += 1
        if (self.gameboard[0][0] == 2 and self.gameboard[1][1] == 2 and
                self.gameboard[2][2] == 2 and self.gameboard[3][3] == 2):
            self.p2_score += 1
        if (self.gameboard[1][1] == 2 and self.gameboard[2][2] == 2 and
                self.gameboard[3][3] == 2 and self.gameboard[4][4] == 2):
            self.p2_score += 1
        if (self.gameboard[2][2] == 2 and self.gameboard[3][3] == 2 and
                self.gameboard[4][4] == 2 and self.gameboard[5][5] == 2):
            self.p2_score += 1
        if (self.gameboard[0][1] == 2 and self.gameboard[1][2] == 2 and
                self.gameboard[2][3] == 2 and self.gameboard[3][4] == 2):
            self.p2_score += 1
        if (self.gameboard[1][2] == 2 and self.gameboard[2][3] == 2 and
                self.gameboard[3][4] == 2 and self.gameboard[4][5] == 2):
            self.p2_score += 1
        if (self.gameboard[2][3] == 2 and self.gameboard[3][4] == 2 and
                self.gameboard[4][5] == 2 and self.gameboard[5][6] == 2):
            self.p2_score += 1
        if (self.gameboard[0][2] == 2 and self.gameboard[1][3] == 2 and
                self.gameboard[2][4] == 2 and self.gameboard[3][5] == 2):
            self.p2_score += 1
        if (self.gameboard[1][3] == 2 and self.gameboard[2][4] == 2 and
                self.gameboard[3][5] == 2 and self.gameboard[4][6] == 2):
            self.p2_score += 1
        if (self.gameboard[0][3] == 2 and self.gameboard[1][4] == 2 and
                self.gameboard[2][5] == 2 and self.gameboard[3][6] == 2):
            self.p2_score += 1

        if (self.gameboard[0][3] == 2 and self.gameboard[1][2] == 2 and
                self.gameboard[2][1] == 2 and self.gameboard[3][0] == 2):
            self.p2_score += 1
        if (self.gameboard[0][4] == 2 and self.gameboard[1][3] == 2 and
                self.gameboard[2][2] == 2 and self.gameboard[3][1] == 2):
            self.p2_score += 1
        if (self.gameboard[1][3] == 2 and self.gameboard[2][2] == 2 and
                self.gameboard[3][1] == 2 and self.gameboard[4][0] == 2):
            self.p2_score += 1
        if (self.gameboard[0][5] == 2 and self.gameboard[1][4] == 2 and
                self.gameboard[2][3] == 2 and self.gameboard[3][2] == 2):
            self.p2_score += 1
        if (self.gameboard[1][4] == 2 and self.gameboard[2][3] == 2 and
                self.gameboard[3][2] == 2 and self.gameboard[4][1] == 2):
            self.p2_score += 1
        if (self.gameboard[2][3] == 2 and self.gameboard[3][2] == 2 and
                self.gameboard[4][1] == 2 and self.gameboard[5][0] == 2):
            self.p2_score += 1
        if (self.gameboard[0][6] == 2 and self.gameboard[1][5] == 2 and
                self.gameboard[2][4] == 2 and self.gameboard[3][3] == 2):
            self.p2_score += 1
        if (self.gameboard[1][5] == 2 and self.gameboard[2][4] == 2 and
                self.gameboard[3][3] == 2 and self.gameboard[4][2] == 2):
            self.p2_score += 1
        if (self.gameboard[2][4] == 2 and self.gameboard[3][3] == 2 and
                self.gameboard[4][2] == 2 and self.gameboard[5][1] == 2):
            self.p2_score += 1
        if (self.gameboard[1][6] == 2 and self.gameboard[2][5] == 2 and
                self.gameboard[3][4] == 2 and self.gameboard[4][3] == 2):
            self.p2_score += 1
        if (self.gameboard[2][5] == 2 and self.gameboard[3][4] == 2 and
                self.gameboard[4][3] == 2 and self.gameboard[5][2] == 2):
            self.p2_score += 1
        if (self.gameboard[2][6] == 2 and self.gameboard[3][5] == 2 and
                self.gameboard[4][4] == 2 and self.gameboard[5][3] == 2):
            self.p2_score += 1



    #Implementation of minimax:
    def minimax(self, depth):
        current_state = copy.deepcopy(self.gameboard)

        for i in range(7):
            if self.make_move(i) != None:
                if self.move_count == 42 or self.depth == 0:
                    self.gameboard = copy.deepcopy(current_state)
                    return i
                else:
                    val = self.minimum(self.gameboard, -infinity, infinity, depth - 1)

                    utility_val[i] = val
                    self.gameboard = copy.deepcopy(current_state)

        max_utility_val = max([i for i in utility_val.values()])

        for i in range(7):
            if i in utility_val:
                if utility_val[i] == max_utility_val:
                    utility_val.clear()
                    return i

    #Max move:
    def maximum(self, current_node, alpha, beta, depth):
        parent = copy.deepcopy(current_node)
        value = -infinity
        children = []

        for i in range(7):
            current_state = self.make_move(i)
            if current_state != None:
                children.append(self.gameboard)
                self.gameboard = copy.deepcopy(parent)

        if children == [] or depth == 0:
            self.count_score(self.gameboard)
            return self.eval_function(self.gameboard)
        else:
            for node in children:
                self.gameBoard = copy.deepcopy(node)
                value = max(value, self.minimum(node, alpha, beta, depth - 1))
                if value >= beta:
                    return value
                alpha = max(alpha, value)
            return value

    #Min move:
    def minimum(self, current_node, alpha, beta, depth):
        parent = copy.deepcopy(current_node)

        if self.current_move == 1:
            opp = 2
        elif self.current_move == 2:
            opp = 1
        value = infinity
        children = []

        for i in range(7):
            current_state = self.check_piece(i, opp)
            if current_state != None:
                children.append(self.gameboard)
                self.gameboard = copy.deepcopy(parent)

        if children == [] or depth == 0:
            self.count_score(self.gameboard)
            return self.eval_function(self.gameboard)
        else:
            for node in children:
                self.gameboard = copy.deepcopy(node)
                value = min(value, self.maximum(node, alpha, beta, depth - 1))
                if value <= alpha:
                    return value
                beta = min(beta, value)
        return value

    #Defining the evaluation function, check README for more info:
    def eval_function(self, state):

        if self.current_move == 1:
            z = 2
        elif self.current_move == 2:
            z = 1

        quad = self.combo_check(state, self.current_move, 4)
        triple = self.combo_check(state, self.current_move, 3)
        double = self.combo_check(state, self.current_move, 2)
        opp_quad = self.combo_check(state, z, 4)
        opp_triple = self.combo_check(state, z, 3)
        opp_double = self.combo_check(state, z, 2)

        return (quad * 10 + triple * 5 + double * 2) - (opp_quad * 10 + opp_triple * 5 + opp_double * 2)

    def change_move(self):
        if self.current_move == 1:
            self.current_move = 2
        elif self.current_move == 2:
            self.current_move = 1

    #Check for cumulative moves by a single player:
    def combo_check(self, state, color, combo):
        count = 0

        for i in range(6):
            for j in range(7):
                if state[i][j] == color:
                    count += self.v_combo_check(i, j, state, combo)
                    count += self.h_combo_check(i, j, state, combo)
                    count += self.d_combo_check(i, j, state, combo)
        return count

    #Check vertically:
    def v_combo_check(self, row, column, state, combo):
        cum_count = 0

        for i in range(row, 6):
            if state[i][column] == state[row][column]:
                cum_count += 1
            else:
                break
        if cum_count >= combo:
            return 1
        else:
            return 0

    #Check horizontally:
    def h_combo_check(self, row, column, state, combo):
        count = 0

        for j in range(column, 7):
            if state[row][j] == state[row][column]:
                count += 1
            else:
                break
        if count >= combo:
            return 1
        else:
            return 0

    #Check diagonally:
    def d_combo_check(self, row, column, state, combo):
        total = 0
        count = 0
        j = column

        for i in range(row, 6):
            if j > 6:
                break
            elif state[i][j] == state[row][column]:
                count += 1
            else:
                break
            j += 1
        if count >= combo:
            total += 1
        count = 0
        j = column
        for i in range(row, -1, -1):
            if j > 6:
                break
            elif state[i][j] == state[row][column]:
                count += 1
            else:
                break
            j += 1
        if count >= combo:
            total += 1
        return total
