class User:
    
    def __init__(self, cliente, username):
        self.cliente = cliente
        self.username = username
        self.inqueue = False
        self.ingame = False
        self.match_id = -1