import unittest
from ConnectNGame.src.player import Player

class TestPlayer(unittest.TestCase):

    def test_get_name(self):
        my_player = Player('sam', '?')
        self.assertEqual(my_player.get_name(),'sam')

    def test_get_piece(self):
        my_player = Player('sam', '?')
        self.assertEqual(my_player.get_piece(),'?')


if __name__ == '__main__':
    unittest.main()
