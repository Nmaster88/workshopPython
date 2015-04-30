#!/usr/bin/python
# -*- coding: utf-8 -*-
from workshopPlayer import *
from workshopGame import *

player1 = Player()
player1.set_name("Miguel")
print player1.get_name()

print player1.get_turn()
player1.set_turn()
print player1.get_turn()
player1.show_board_main()
player1.show_board_fire()

game = Game()
game.add_player()
game.add_player()
