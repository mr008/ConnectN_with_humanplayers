
class Player(object):
    def __init__(self,name: str, piece: str) -> None:
        self.name = name
        self.piece = piece


    def get_name(self) -> None:
        return self.name

    def get_piece(self) -> None:
        return self.piece

