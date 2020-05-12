import unittest
from unittest.mock import patch
from .print_capturer import PrintCapturer
from ConnectNGame.src.board import Board

class TestBoard(unittest.TestCase):

    def test_place_piece(self):
        my_board = Board(4,6,'$')
        my_board.place_piece(3,2,'#')
        self.assertEqual(my_board.my_list[3][2],"#")

    def test_check_full(self):
        board1 = Board(3, 3, "*")
        board1.my_list = ("***", "*", "**")
        bool =board1.check_full(1)
        self.assertEqual(bool, False)




    def test_print_board(self):
        board1=Board(3,3,"*")
        capture = PrintCapturer()
        with patch('ConnectNGame.src.board.Board.print_board', side_effect=capture):
            board1.print_board()
            answer = [" 012",
                  "0***",
                  "1***",
                  "2***"]
            self.assertEqual(answer, capture.output)


if __name__ == '__main__':
    unittest.main()
