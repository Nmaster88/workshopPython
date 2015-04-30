#!/usr/bin/python
# -*- coding: utf-8 -*-
from workshopPlayer import Player
from random import random


class Game(object):

    def __init__(self):
        self.name = "Battleship"
        self.player = []

    def add_player(self):
        print "Insert Player Name: ",
        player = Player()
        #player.set_name(raw_input())
        player.set_name("Miguel")
        print "Added player " + player.get_name()

    def coinToss(self):
        if(random() > 0.5):
            return 2
        else:
            return 1

    def start(self):
        print "Welcome to " + self.name
        self.add_player()
        self.add_player()
        toss = self.coinToss()
        # Definir o turno do jogador que calhar a moeda
        # Colocar navios no board do jogador 1
        # Colocar navios no board do jogador 2
        self.main_loop()

    def main_loop(self):
        * Verificar se algum jogador tem o board de navios a 0
           + Se algum jogador tiver o tabuleiro a zeros, perde 
        * Verificar qual o turno dos jogadores
            + Ver tabuleiro dos navios
            + Ver tabuleiro de disparo  
            + Disparar
                - Muda de turno

                
        pass

