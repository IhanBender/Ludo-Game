class User:

    def __init__(self, username):
        self.username = username
        self.inqueue = False
        self.ingame = False
        self.match_id = -1
        self.playerIndex = -1