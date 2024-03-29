import ConnectNGame
from ConnectNGame.src.game import Game


class Config(object):

    def get_from_file(self, config_address: str)-> Game:
        # config_address=str(sys.argv[1])
        # config_address = "E:\\coding programs\\ConnectN\\config_files\\3X3X3.txt"
        # config_address = "/Users/audeclairemoats/PycharmProject/ConnectN/config_files/3X3X3.txt"
        board_config = {}
        with open(config_address) as ca:
            for line in ca:
                key, index = line.strip().split(':')
                board_config[key.strip()] = index.strip()
        blank_char = board_config["blank_char"]
        num_rows = board_config["num_rows"]
        num_pieces_to_win = board_config["num_pieces_to_win"]
        num_cols = board_config["num_cols"]
        return ConnectNGame.src.game.Game(blank_char, num_rows, num_pieces_to_win, num_cols)
