import copy
from typing import Tuple
class Board(object):
    def __init__(self,ro: int, col: int, bla: str) -> None:
        self.rows = int(ro)
        self.cols = int(col)
        self.blank = bla
        self.my_list = []
        self.in_my_list = []
        for j in range(self.cols):
            self.in_my_list.append(self.blank)
        for i in range(self.rows):
            self.my_list.append(copy.deepcopy(self.in_my_list))
        self.contents = [[self.blank for col in range(self.cols)] for row in range(self.rows)]

    def __getitem__(self, item: Tuple[int,int]) -> str:
        x,y=item
        return self.my_list[x][y]

    def place_piece(self, row: int, col: int, symbol: str) -> None:
        self.my_list[row][col] = symbol

    def get_cols(self) -> int:
        return self.cols

    def get_blank(self) -> str:
        return self.blank

    def from_my_list(self,r: int,c:int) -> str:
        return self.my_list[r][c]

    def get_my_list(self) -> list:
        return self.my_list

    def get_in_my_list(self) -> list:
        return self.in_my_list

    def check_full(self,col: int) -> bool:
        count = 0
        for i in range(self.rows):
            if(self.my_list[i][col] != self.blank):
                count+=1
        if count == self.rows:
            return True
        return False

    def __str__(self) -> str:
        to_print = ' '
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