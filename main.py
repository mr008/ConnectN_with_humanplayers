#Ok! Wish us good luck!
import sys
from ConnectNGame.src.game import Game
from ConnectNGame.src.config import Config


def main() -> None:

    config1=Config()
    config_address=str(sys.argv[1])
    game1=config1.get_from_file(config_address)
    game1.setup_players()
    game1.start_game()





if __name__ == '__main__':
    main()
