import sys
from ConnectNGame.src.player import Player
from ConnectNGame.src.board import Board
class Game(object):
    def __init__(self,blank_char: str,num_rows: str,num_pieces_to_win: str,num_cols: str) -> None:
        self.players = []
        self.blank_char = blank_char
        self.num_rows = int(num_rows)
        self.num_pieces_to_win = int(num_pieces_to_win)
        self.num_cols = int(num_cols)
        self.board = Board(self.num_rows,self.num_cols,blank_char)
        self.current = 0

    def switch_player(self) -> None:
        self.current += 1
        if (self.current == 2):
            self.current = 0
    def get_player(self, num: int) -> Player:
        return self.players[num]

    def get_num_cols(self)-> int:
        return self.num_cols

    def get_num_rows(self) -> int:
        return self.num_rows

    def get_board(self) -> Board:
        return self.board

    def get_current(self) -> int:
        return self.current

    def setup_players(self) -> None:
        while True:
            try:
                playname1 = input('Player 1 enter your name: ')
            except ValueError:
                    print('Your name cannot be the empty string or whitespace.')
                    continue
            break
        while True:
            try:
                playpiece1 = input('Player 1 enter your piece: ')
                if ((playpiece1 != '') & (playpiece1 != ' ') & (playpiece1 != self.board.get_blank()) & (len(playpiece1) == 1)):
                    break
                elif ((playpiece1 == '')| (playpiece1 == ' ')):
                    raise ValueError('Your piece cannot be the empty string or whitespace.')
                elif (playpiece1 == self.board.get_blank()):
                    raise ValueError('Your piece cannot be the same as the blank character.')
                elif (len(playpiece1) != 1 ):
                    raise ValueError('{} is not a single character. Your piece can only be a single character.'.format(playpiece1))
            except ValueError as r:
                print(r)
        player1 = Player(playname1,playpiece1)
        while True:
            try:
                playname2 = input('Player 2 enter your name: ')
                if ((playname2 != '') & (playname2 != ' ')& (playname2.lower() != playname1.lower())):
                    break
                elif((playname2 == '') | (playname2 == ' ')):
                    raise ValueError('Your name cannot be the empty string or whitespace.')
                elif(playname2.lower() == playname1.lower()):
                    raise ValueError('You cannot use {} for your name as someone else is already using it.'.format(playname2))
            except ValueError as r:
                print(r)
        while True:
            try:
                playpiece2 = input('Player 2 enter your piece: ')
                if ((playpiece2 != '') & (playpiece2 != ' ') & (playpiece2 != self.board.get_blank()) & (len(playpiece2) == 1) & (playpiece2 != playpiece1)):
                    break
                elif ((playpiece2 == '')| (playpiece2 == ' ')):
                    raise ValueError('Your piece cannot be the empty string or whitespace.')

                elif (playpiece2 == self.board.get_blank()):
                    raise ValueError('Your piece cannot be the same as the blank character.')

                elif (len(playpiece2) != 1 ):
                    raise ValueError('{} is not a single character. Your piece can only be a single character.'.format(playpiece2))

                elif (playpiece2 == playpiece1):
                    raise ValueError('You cannot use {} for your piece as {} is already using it.'.format(playpiece2,player1.get_name()))
            except ValueError as r:
                print(r)
        player2 = Player(playname2,playpiece2)
        self.players.append(player1)
        self.players.append(player2)
        return

    def check_har_win(self,player: Player) -> bool:
        for rows in range(self.board.rows):
            counter = 0
            for cols in range(self.board.cols):
                if self.board[(rows,cols)] == self.board.get_blank():
                    counter = 0
                if self.board[(rows,cols)] == player.get_piece():
                    counter += 1
                    if counter == self.num_pieces_to_win:
                        return True

        return False

    def check_left_obl(self,player: Player) -> bool:
        for cols in range(self.board.cols):
            counter = 0
            step=0
            for rows in range(self.board.rows):
                step+=1
                if self.board[(rows,cols)] == self.board.get_blank():
                    counter = 0
                    step=0
                if self.board[(rows,cols-step)] == player.get_piece():
                    counter += 1
                    if counter == self.num_pieces_to_win:
                        return True

        return False
    def check_right_obl(self,player: Player) -> bool:
        for cols in range(self.board.get_cols()):
            counter = 0
            step=0
            for rows in range(self.board.rows):
                if self.board[(rows,cols)] == self.board.get_blank():
                    counter = 0
                    step=0
                if rows<self.board.rows and cols+step<self.board.cols:
                    if self.board[(rows,cols+step)] == player.get_piece():
                        counter += 1
                        step += 1
                        if counter == self.num_pieces_to_win:
                            return True


        return False



    def check_ver_win(self,player: Player) -> bool:
        for cols in range(self.board.cols):
            counter=0
            for rows in range(self.board.rows):
                if self.board[(rows,cols)] == self.board.get_blank():
                    counter=0
                if self.board[(rows,cols)] == player.get_piece():
                    counter+=1
                    if counter == self.num_pieces_to_win:
                        return True
        return False

    def check_all_win(self,player: Player) -> bool:
        win1 = self.check_ver_win(player)
        win2 = self.check_right_obl(player)
        win3 = self.check_left_obl(player)
        win4 = self.check_har_win(player)
        all_wins = [win1,win2,win3,win4]
        return any(all_wins)



    def start_game(self) -> None:
        self.setup_players()
        print(self.board)
        while True:
            playcol1 = int(input('{}, please enter the column you want to play in: '.format(self.get_player(self.get_current()).get_name())))
            if (type(playcol1) != int):
                print('{}, column needs to be an integer.{} is not an integer.'.format(self.get_player(self.get_current()).get_name(), playcol1))
                continue
            else:
                for i in range(self.get_num_rows() - 1, -1, -1):
                    if (self.get_board().from_my_list(i, playcol1) == self.get_board().get_blank()):
                        self.get_board().place_piece(i, playcol1, self.get_player(self.get_current()).get_piece())
                        print(self.get_board())
                        break
            if self.check_all_win(self.get_player(self.get_current())) :
                print('{} won the game!'.format(self.get_player(self.get_current()).get_name()))
                break
            self.switch_player()



