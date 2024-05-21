class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.x = 50
        self.y = 50
    def get_pos(self):
        return self.x, self.y
    def set_pos(self, x, y):
        self.x = x
        self.y = y
        return self.x, self.y
