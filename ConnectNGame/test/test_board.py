import unittest
from ConnectNGame.src.board import Board


class TestBoard(unittest.TestCase):

    def test_place_piece(self):
        my_board = Board(4, 6, '$')
        my_board.place_piece(3, 2, '#')
        self.assertEqual(my_board.my_list[3][2], "#")
        my_board2 = Board(4, 3, '%')
        my_board2.place_piece(0, 0, '*')
        self.assertEqual(my_board2.my_list[0][0], '*')

    def test_check_full(self):
        board1 = Board(3, 3, "*")
        for i in range(2):
            board1.my_list[i][1] = '^'
        bool1 = board1.check_full(1)
        self.assertEqual(bool1, False)
        board2 = Board(6, 6, "&")
        for j in range(6):
            board2.my_list[j][3] = "%"
        check = board2.check_full(3)
        self.assertEqual(True, check)

        board3 = Board(5, 4, '^')
        for k in range(5):
            board3.my_list[k][0] = '*'
        check2 = board3.check_full(0)
        self.assertEqual(check2, True)


if __name__ == '__main__':
    unittest.main()
