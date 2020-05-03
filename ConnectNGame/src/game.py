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
            playname1 = input('Player 1 enter your name: ')
            if (playname1 != '' & playname1 != ' '):
                break
            else:
                print('Your name cannot be the empty string or whitespace.')
                continue
         while True:
                playpiece1 = input('Player 1 enter your piece: ')
                if (playpiece1 != '' & playpiece1 != ' ' & playpiece1 != self.board.blank & len(playpiece1) == 1):
                    break
                elif (playpiece1 == ''| playpiece1 == ' '):
                    print('Your piece cannot be the empty string or whitespace')
                    continue
                elif (playpiece1 == self.board.blank):
                    print('Your piece cannot be the same as the blank character.')
                    continue
                elif (len(playpiece1) != 1 ):
                    print('{} is not a single character. Your piece can only be a single character.'.format(playpiece1))
                    continue
        player1 = Player(playname1,playpiece1)
        while True:
            playname2 = input('Player 2 enter your name: ')
            if (playname2 != '' & playname2 != ' '& playname2.lower() != playname1.lower()):
                break
            elif(playname2 == '' | playname2 == ' '):
                print('Your name cannot be the empty string or whitespace.')
                continue
            elif(playname2.lower() == playname1.lower()):
                print('You cannot use {name} for your name as someone else is already using it.'.format(playname2))
                continue

        while True:
            playpiece2 = input('Player 2 enter your piece')
            if (playpiece2 != '' & playpiece2 != ' ' & playpiece2 != self.board.blank & len(playpiece2) == 1 & playpiece2 != playpiece1):
                break
            elif (playpiece2 == ''| playpiece2 == ' '):
                print('Your piece cannot be the empty string or whitespace')
                continue
            elif (playpiece2 == self.board.blank):
                print('Your piece cannot be the same as the blank character.')
                continue
            elif (len(playpiece2) != 1 ):
                print('{} is not a single character. Your piece can only be a single character.'.format(playpiece2))
                continue
            elif (playpiece2 == playpiece1):
                print('You cannot use {piece} for your piece as {player} is already using it.'.format(playpiece2,player1.name))
        player2 = (playname2,playpiece2)
        self.players.append(player1)
        self.players.append(player2)
    def setup_board(self):

    def plears_turn(self):
        ...

    def check_ver_win(self):
        ...
    def check_obli_win(self):

    def check_har_win(self):

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
        while True:
            while True:
                playcol1 = input('{},please enter the column you want to play in'.format(self.players[0].name) )
                if (type(playcol1) != int):
                    print('{} column needs to be an integer.{} is not an integer.'.format(self.players[0].name,playcol1))
                    continue
                else:
                    for i in range(self.num_cols-1,-1,-1):
                        if (self.board.my_list[i][playcol1] == self.blank_char):
                            self.board.place_piece(i,playcol1,self.players[0].piece)
                            print(self.board)
                            break
                break
            while True:
                playcol2 = input('{] please enter the column you want to play in'.format(self.players[1].name))
                if (type(playcol2 != int)):
                    print('{} column needs to be an integer.{} is not an integer.'.format(self.players[1].name,playcol2))
                    continue
                else:
                    for i in range(self.num_cols-1,-1,-1):
                        if (self.board.my_list[i][playcol2] == self.blank_char):
                            self.board.place_piece(i,playcol2,self.players[1].piece)
                            print(self.board)
                            break
                break
            continue


