import unittest
from ConnectNGame.src.player import Player
from unittest.mock import patch
from ConnectNGame.src.board import Board
from ConnectNGame.src.game import Game

class TestGame(unittest.TestCase):

    def test_switch_player(self):
        my_game = Game('*','6','4','6')
        my_game.switch_player()
        my_game.switch_player()
        my_game.switch_player()
        self.assertEqual(my_game.current,1)

    def test_har_win(self):
        game1 = Game('*','6','4','6')
        test_player = Player('sam','@')
        for i in range(4):
            game1.board.place_piece(3,i,'@')
        win = game1.check_har_win(test_player)
        self.assertEqual(True,win)



    def test_check_left_obl(self):
        testgame=Game("*","3","3","3")
        testplayer=Player("#","#")
        testgame.board.place_piece(2, 0, '#')
        testgame.board.place_piece(1,1,"#")
        testgame.board.place_piece(0,2,"#")
        bool=testgame.check_left_obl(testplayer)
        self.assertEqual(bool,True)

        testgame = Game("*", "3", "3", "3")
        testplayer = Player("#", "#")
        testgame.board.place_piece(0, 0, '#')
        testgame.board.place_piece(1, 1, "#")
        testgame.board.place_piece(2, 2, "#")
        bool = testgame.check_left_obl(testplayer)
        self.assertEqual(bool, False)

    def test_check_right_obl(self):
        testgame = Game("*", "3", "3", "3")
        testplayer = Player("#", "#")
        testgame.board.place_piece(0, 0, '#')
        testgame.board.place_piece(1, 1, "#")
        testgame.board.place_piece(2, 2, "#")
        bool = testgame.check_right_obl(testplayer)
        self.assertEqual(bool, True)

        testgame = Game("*", "3", "3", "3")
        testplayer = Player("#", "#")
        testgame.board.place_piece(2, 0, '#')
        testgame.board.place_piece(1, 1, "#")
        testgame.board.place_piece(0, 2, "#")
        bool = testgame.check_right_obl(testplayer)
        self.assertEqual(bool, False)

    def test_ver_win(self):
        game2 = Game('*', '6', '4', '6')
        test_player = Player('sam', '@')
        for i in range(4):
            game2.board.place_piece(i, 4, '@')
        win = game2.check_ver_win(test_player)
        self.assertEqual(True, win)


    def test_setup_player(self):
        my_game = Game('*', '6', '4', '6')
        user_input = ['sam','$','jess','&']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            my_game.setup_players()
        self.assertEqual(my_game.players[0].get_name(),'sam')
        self.assertEqual(my_game.players[0].get_piece(),'$')
        self.assertEqual(my_game.players[1].get_name(), 'jess')
        self.assertEqual(my_game.players[1].get_piece(),'&')




if __name__ == '__main__':
    unittest.main()
