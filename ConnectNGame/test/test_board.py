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
        for i in range(2):
            board1.my_list[i][1] = '^'
        bool = board1.check_full(1)

        self.assertEqual(bool, False)
        board2 = Board(6,6,"&")
        for j in range(6):
            board2.my_list[j][3] = "%"
        check = board2.check_full(3)
        self.assertEqual(True,check)

        board3 = Board(5,4,'^')
        for k in range(5):
            board3.my_list[k][0] = '*'
        check2 = board3.check_full(0)
        self.assertEqual(check2, True)




    def test_print_board(self):
        """"
        board1=Board(3,3,"*")
        capture = PrintCapturer()
        with patch('ConnectNGame.src.board.Board.print_board', side_effect=capture):
            board1.print_board()
            answer = [" 012",
                  "0***",
                  "1***",
                  "2***"]
            self.assertEqual(answer, capture.output)
        """


if __name__ == '__main__':
    unittest.main()
