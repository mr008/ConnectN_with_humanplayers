import unittest
from unittest.mock import patch
from .print_capturer import PrintCapturer
from ConnectNGame.src.board import Board

class TestBoard(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
    def test_print_piece(self):
        ...

    def test_check_full(self):
        board1 = Board(3, 3, "*")
        board1.my_list = ("***", "*", "**")
        bool =board1.check_full(1)
        self.assertEqual(bool, False)




    def test_print_list(self):
        board1=Board(3,3,"*")
        capture = PrintCapturer()
        with patch('ConnectNGame.src.board.Board', side_effect=capture):
            print(board1)
            answer = [" 012",
                  "0***",
                  "1***",
                  "2***"]
            self.assertEqual(answer, capture.output)


if __name__ == '__main__':
    unittest.main()
