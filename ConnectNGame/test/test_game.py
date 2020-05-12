import unittest
from ConnectNGame.src.game import Game

class TestGame(unittest.TestCase):

    def test_switch_player(self):
        my_game = Game('*','6','4','6')
        my_game.switch_player()
        my_game.switch_player()
        my_game.switch_player()
        self.assertEqual(my_game.current,1)
    def test_har_win(self):
        self.assertEqual(True, False)

    def test_check_left_obl(self):

    def test_check_right_obl(self):

    def test_ver_win(self):

    def test_setup_player(self):


if __name__ == '__main__':
    unittest.main()
