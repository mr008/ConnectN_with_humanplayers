#Ok! Wish us good luck!
import sys
from ConnectNGame.src.game import Game
def main() -> None:
    config_address=str(sys.argv[1])
    game1=Game.get_from_file(config_address)
    game1.start

if __name__ == '__main__':
    main()
