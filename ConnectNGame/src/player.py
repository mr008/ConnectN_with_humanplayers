
class Player(object):
    def __init__(self,name: str, piece: str) -> None:
        self.name = name
        self.piece = piece


    def get_name(self) -> str:
        return self.name

    def get_piece(self) -> str:
        return self.piece

