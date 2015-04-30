#!/usr/bin/python
# -*- coding: utf-8 -*-


class Player(object):

    def __init__(self):
        self.name = ""
        self.turn = False
        self.board_main = [[0 for i in range(10)] for j in range(10)]
        self.board_fire = [[0 for i in range(10)] for j in range(10)]

    def validadeCoodinates(self, x, y):
        if x >= 0 and x < 10 and y >= 0 and y < 10:
            print "Valid coodinates"
            return True
        else:
            print "Invalid coordinates"
            return False

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def set_turn(self):
        if self.turn == True:
            self.turn = False
        else:
            self.turn = True

    def get_turn(self):
        return self.turn

    def get_board_main(self):
        return self.board_main

    def get_board_fire(self):
        return self.board_fire

    def set_board_main(self, x, y, type_mark):
        # If coodinates are in the scope
        if(self.validadeCoodinates(x, y)):
            # Set a boat
            self.board_main[x][y] = type_mark
            return True
        else:
            return False

    def set_board_fire(self, x, y, type_mark):
        # If coodinates are in the scope
        if(self.validadeCoodinates(x, y)):
            # Set a fire
            self.board_fire[x][y] = type_mark
            return True
        else:
            return False

    def show_board_main(self):
        rowNumber = 0
        print "Board:\n  |",
        for i in range(0, 10):
            print i,
        print "|"
        print "-" * 25,
        print
        for row in self.get_board_main():
            print str(rowNumber) + " |",
            for col in row:
                print col,
            print "|"
            rowNumber += 1

    def show_board_fire(self):
        rowNumber = 0
        print "Board:\n  |",
        for i in range(0, 10):
            print i,
        print "|"
        print "-" * 25,
        print
        for row in self.get_board_fire():
            print str(rowNumber) + " |",
            for col in row:
                print col,
            print "|"
            rowNumber += 1
