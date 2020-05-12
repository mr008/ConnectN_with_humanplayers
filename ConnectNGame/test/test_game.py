import unittest
from unittest.mock import patch
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
        game1.setup_players()
        game1.board()
        game1.check_har_win(game1.players[0])
        self.assertEqual()



    def test_check_left_obl(self):
        pass

    def test_check_right_obl(self):
        pass

    def test_ver_win(self):
        game2 = Game('*', '6', '4', '6')


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
