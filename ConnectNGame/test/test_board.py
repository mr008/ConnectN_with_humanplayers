import unittest
from unittest.mock import patch
from .print_capturer import PrintCapturer
from ConnectNGame.src.board import Board

class TestBoard(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
    def test_print_piece(self):

    def test_check_full(self):




    def test_print_list(self):
        values = [4, 5, 'hi', 'bye']
        capture = PrintCapturer()
        with patch('ConnectNGame.src.example_printing.print', side_effect=capture):
            print_list(values)
            answer = ['4\n', '5\n', 'hi\n', 'bye\n']
            self.assertEqual(answer, capture.output)


if __name__ == '__main__':
    unittest.main()
