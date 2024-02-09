#make a new user player 
class Player:
    #initialazation user
    def __init__(self, username, conn):
        self.userN = username
        self.conn = conn
        self.state = "loggedin"
    
    #send message to the connected
    def send(self, msg):
        self.conn.send(msg)

    #set user available for playing
    def setAval(self):
        self.state = "A"

    #set user busy for play 
    def Busy(self):
        self.state = "busy"

    #set user logged in for play
    def login(self):
        self.state = "loggedin"
    
    