import copy
class Board(object):
    def __init__(self,ro: int, col: int, bla: str) -> None:
        self.rows = ro
        self.cols = col
        self.blank = bla
        self.my_list = []
        self.in_my_list = []
        for j in range(self.cols):
            self.in_my_list.append(self.blank)
        for i in range(self.rows):
            self.my_list.append(copy.deepcopy(self.in_my_list))
        self.contents = [[self.blank for col in range(self.cols)] for row in range(self.rows)]

    def __getitem__(self, item) -> list:
        return self.contents

    def place_piece(self, row: int, col: int, symbol: str) -> None:
        self.my_list[row][col] = symbol
    def check_full(self):
        ...
    def get_piece(self):
        ...
    def get_blank(self):
        return self.blank

    def get_my_list(self,r,c):
        return self.my_list[r][c]

    def get_in_my_list(self,r,c):
        return self.in_my_list[r][c]

    def __str__(self) -> None:
        for k in range(self.cols):
            to_print += ' ' + str(k)
        to_print += '\n'
        for i in range(self.rows):
            to_print += str(i)
            for j in range(self.cols):
                to_print += ' ' + self.my_list[i][j]
            if (i < (self.rows - 1)):
                to_print += '\n'
        return (to_print)