#Ok! Wish us good luck!
import sys
from ConnectNGame.src.game import Game
def main() -> None:
    config_address=str(sys.argv[1])
    game1 = Game.get_from_file(config_address)
    game1.setup_players()
    game1.start_game()



while True:
    playcol1 = input('{}, please enter the column you want to play in'.format(game1.get_player(game1.get_current()).get_name()))
    if (type(playcol1) != int):
        print('{}, column needs to be an integer.{} is not an integer.'.format(game1.get_player(game1.get_current()).get_name(), playcol1))
        continue
    else:
        for i in range(game1.get_num_rows() - 1, -1, -1):
            if (game1.get_board().get_my_list(i,playcol1) == game1.get_board().get_blank()):
                game1.get_board().place_piece(i, playcol1, game1.get_player(game1.get_current()).get_piece())
                print(game1.get_board())
                break
    if (game1.check_har_win(game1.get_player(game1.get_current())) | game1.check_ver_win(game1.get_player(game1.get_current())) | game1.check_obli_win(game1.get_player(game1.get_current()))):
        print('{} won the game!'.format(game1.get_player(game1.get_current()).get_name()))
        break
    game1.switch_player()

if __name__ == '__main__':
    main()
