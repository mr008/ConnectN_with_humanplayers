#Ok! Wish us good luck!
import sys
from ConnectNGame.src.game import Game
from ConnectNGame.src.config import Config


def main() -> None:

    config1=Config()
    #config_address=str(sys.argv[1])'
    config_address = "E:\\coding programs\\ConnectN\\config_files\\3X3X3.txt"
    game1=config1.get_from_file(config_address)
    game1.start_game()


if __name__ == '__main__':
    main()
#"/Users/audeclairemoats/PycharmProject/ConnectN/config_files/3X3X3.txt""E:\\coding programs\\ConnectN\\config_files\\3X3X3.txt"