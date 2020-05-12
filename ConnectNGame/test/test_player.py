import unittest
from ConnectNGame.src.player import Player

class TestPlayer(unittest.TestCase):

    def test_get_name(self):
        my_player = Player('sam', '?')
        self.assertEqual(my_player.get_name(),'sam')

        my_player = Player('', '?')
        self.assertEqual(my_player.get_name(), '')

        my_player = Player('ALFJDSLFJADSLKFJADSKLFJADSJFDASKLFJDASKJFLADSJFDASLKFJADSKFJ', '%')
        self.assertEqual(my_player.get_name(), 'ALFJDSLFJADSLKFJADSKLFJADSJFDASKLFJDASKJFLADSJFDASLKFJADSKFJ')

    def test_get_piece(self):
        my_player = Player('sam', '?')
        self.assertEqual(my_player.get_piece(),'?')

        my_player = Player('1', '!')
        self.assertEqual(my_player.get_piece(), '!')

        my_player = Player('SFAS', '')
        self.assertEqual(my_player.get_piece(), '')


if __name__ == '__main__':
    unittest.main()
