class Board(object):
    def __init__(self, name: str, ro: int, col: int, bla: str) -> None:
        self.rows = ro
        self.cols = col
        self.blank = bla
        self.my_list = []
        self.name = name
        self.in_my_list = []
        for j in range(self.cols):
            self.in_my_list.append(self.blank)
        for i in range(self.rows):
            self.my_list.append(copy.deepcopy(self.in_my_list))

    def place_char(self, row: int, col: int, symbol: str) -> None:
        self.my_list[row][col] = symbol

    def __str__(self) -> None:
        to_print = self.name
        to_print += '\n'
        to_print += ' '
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