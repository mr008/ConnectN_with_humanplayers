import sys
from ConnectNGame.src.player import Player
class Game(object):
    def __init__(self,blank_char,num_rows,num_pieces_to_win,num_cols):
        self.players = []
        self.cr_player = current_player
        self.blank_char = blank_char
        self.num_rows = num_rows
        self.num_pieces_to_win = num_pieces_to_win
        self.num_cols = num_cols
        self.board = Board(num_rows,num_cols,blank_char)

    def setup_players(self):
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
                if (playpiece1 != '' & playpiece1 != ' ' & playpiece1 != self.board.blank & len(playpiece1) == 1):
                    break
                elif (playpiece1 == ''| playpiece1 == ' '):
                    raise ValueError('Your piece cannot be the empty string or whitespace')
                elif (playpiece1 == self.board.blank):
                    raise ValueError('Your piece cannot be the same as the blank character.')
                elif (len(playpiece1) != 1 ):
                    raise ValueError('{} is not a single character. Your piece can only be a single character.'.format(playpiece1))
            except ValueError as r:
                print(r)
        player1 = Player(playname1,playpiece1)
        while True:
            try:
                playname2 = input('Player 2 enter your name: ')
                if (playname2 != '' & playname2 != ' '& playname2.lower() != playname1.lower()):
                    break
                elif(playname2 == '' | playname2 == ' '):
                    raise ValueError('Your name cannot be the empty string or whitespace.')
                elif(playname2.lower() == playname1.lower()):
                    raise ValueError('You cannot use {name} for your name as someone else is already using it.'.format(playname2))
            except ValueError as r:
                print(r)

        while True:
            try:
                playpiece2 = input('Player 2 enter your piece')
                if (playpiece2 != '' & playpiece2 != ' ' & playpiece2 != self.board.blank & len(playpiece2) == 1 & playpiece2 != playpiece1):
                    break
                elif (playpiece2 == ''| playpiece2 == ' '):
                    raise ValueError('Your piece cannot be the empty string or whitespace')
                elif (playpiece2 == self.board.blank):
                    raise ValueError('Your piece cannot be the same as the blank character.')
                elif (len(playpiece2) != 1 ):
                    raise ValueError('{} is not a single character. Your piece can only be a single character.'.format(playpiece2))
                elif (playpiece2 == playpiece1):
                    raise ValueError('You cannot use {piece} for your piece as {player} is already using it.'.format(playpiece2,player1.name))
            except ValueError as r:
                print(r)
        player2 = (playname2,playpiece2)
        self.players.append(player1)
        self.players.append(player2)
    def setup_board(self):

    def plears_turn(self):
        ...

    def check_har_win(self,player):
        for rows in range(self.board.my_list):
            counter = 0
            for cols in range(self.board.in_my_list):
                if self.board[rows][cols] == self.board.blank:
                    counter = 0
                if self.board[rows][cols] == player.get_piece():
                    counter += 1
                    if counter == self.num_pieces_to_win:
                        return True
        else:
            return False
    def check_obli_win(self):
        consecutive_items = 0
        last_seen_item = None
        for lists in self.board.my_list
            for item in lists:
                if item == self.blank_char:
                    consecutive_items = 0
                elif item == last_seen_item:
                    consecutive_items += 1
                else:
                    consecutive_items = 1
                last_seen_item = item
                if consecutive_items == 4:
                    return True
            return False


    def check_ver_win(self,player):
        for cols in range(self.board.in_my_list):
            counter=0
            for rows in range(self.board.my_list):
                if self.board[rows][cols] == self.board.blank:
                    counter=0
                if self.board[rows][cols] == player.get_piece():
                    counter+=1
                    if counter == self.num_pieces_to_win:
                        return True
        else:
            return False
    def change_player(self):


    def declare_win(self):
        ...
    def add_piece(self):

    def get_from_file(self,config_address):
        # config_address=str(sys.argv[1])
        #config_address = "E:\\coding programs\\ConnectN\\config_files\\3X3X3.txt"
        board_config = {}
        with open(config_address) as ca:
            for line in ca:
                key, index = line.strip().split(':')
                board_config[key.strip()] = index.strip()
        blank_char = board_config["blank_char"]
        num_rows = board_config["num_rows"]
        num_pieces_to_win = board_config["num_pieces_to_win"]
        num_cols = board_config["num_cols"]
        return Game(blank_char,num_rows,num_pieces_to_win,num_cols)

    def start_game(self):
        self.setup_players()
        print(self.board)
        #Can put in main if better
        while True:
            while True:
                playcol1 = input('{}, please enter the column you want to play in'.format(self.players[0].get_name) )
                if (type(playcol1) != int):
                    print('{}, column needs to be an integer.{} is not an integer.'.format(self.players[0].get_name,playcol1))
                    continue
                else:
                    for i in range(self.num_cols-1,-1,-1):
                        if (self.board.my_list[i][playcol1] == self.blank_char):
                            self.board.place_piece(i,playcol1,self.players[0].get_piece)
                            print(self.board)
                            break
                if (self.check_har_win(self.players[0]) | self.check_ver_win(self.players[0]) | self.check_obli_win(self.players[0])):
                    print('{} won the game!'.format(self.players[0].get_name))
                    return
                break
            while True:
                playcol2 = input('{], please enter the column you want to play in'.format(self.players[1].get_name))
                if (type(playcol2 != int)):
                    print('{}, column needs to be an integer.{} is not an integer.'.format(self.players[1].get_name,playcol2))
                    continue
                else:
                    for i in range(self.num_cols-1,-1,-1):
                        if (self.board.my_list[i][playcol2] == self.blank_char):
                            self.board.place_piece(i,playcol2,self.players[1].get_piece)
                            print(self.board)
                            break
                if (self.check_har_win(self.players[0]) | self.check_ver_win(self.players[0]) | self.check_obli_win(self.players[0])):
                    print('{} won the game!'.format(self.players[0].get_name))
                    return
                break
            continue


