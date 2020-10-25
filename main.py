from player import Player
from board import Board
from game import Game

import globals
import random

globals.init()

def main():
    # set board and player with card instances
    board = Board(globals.decks['Quest Deck'], globals.decks['Encounter Deck'], [], [], [])
    player = Player(globals.decks['Player Deck'], globals.heroes, [], [], 25)

    # init game and ready player
    game = Game(board, player)
    game.setupGame()

    # simulate game to end state
    turns = 0
    while 1:
        game.doTurn()
        print(f'turn: {turns}')
        turns += 1
        if globals.gameOver:
            print(f'game lost')
            break
        if globals.gameWin:
            print(f'game win')
            break

    globals.gameWin = False
    globals.gameOver = False

if __name__ == "__main__":
    main()

