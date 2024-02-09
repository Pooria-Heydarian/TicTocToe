import socket
import sys 
import time
import _thread
from player import Player
from board import Board

import uuid #Universally Unique Identifier generator for player
from threading import RLock, Thread
help_command  = "Commands List:\nwho- Show all players that logged in.\ngames- Show Games List That already in proccess.\nlogin username- Endter login followd by a username of your choise.\n play- Finds and starts a game.\nplace n- Move to position n, where n is in range of [0,8].\nexit- Leave the server." 
#Create server socket object
try:
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print('Could not create socket')


#Bind to port 6969
try:
    socket.bind(('', 6969))
except socket.error:
    print ('Failed')
    sys.exit()

#listening to socket
socket.listen(5)
print ("Listening in port 6969 .....")

#Stored UUID object, keeps games currently underway
games = []

#Keeps players currently in the server
players=[]

#define Lock
lock = RLock() #use RLOCK instead of LOCK becuase we wanna to aquire this multiple times, by the same thread.

#checking move that is it valid move !?
def check(game,move):
    try:
        ord , pos = move.split(" ")
        pos = int(pos)
    except ValueError: 
        return False
    
    #Check that order is in true syntax
    if ord != "place":
        return False

    # Check position is in valid range([1,8]) and this place is empty
    elif pos > 8 and pos < 0 and game.board[pos] == "X" and game.board[pos] == "O":
        return False

    else:
        return True  
    
def start(game):
    #main game loop 
    End_OF_Game = False
    while not End_OF_Game:
        # Send Turn message for gamers
        game.turn.send("Your Turn, Good Luck!".encode())
        game.waiting.send("Wait, not your turn!".encode())
        
        #get move 
        move = game.turn.conn.recv(4096).decode()

        # processing move
        if check(game,move):
            respon = game.makeMove(move.split(" ")[1])

            if respon == "301 NPT":
                msg = "WAIT"+game.drawBoard()
                game.turn.send(msg.encode())
                game.waiting.send(msg.encode())
                game.changeTurn()

            elif respon == "300 FIN":
                End_OF_Game = True
                game.turn.send("No winner".encode())
                game.waiting.send("No winner".encode())

            elif respon == "300 WIN":
                End_OF_Game = True
                game.turn.send("Game over, You Won!".encode())
                msg = "Game Over."+game.turn.userN+" Won!"
                game.waiting.send(msg.encode())
                print("Game Over!")
        else:
            continue
    return

def connect(clientSock):
    """Handles mesaage sent from the client and send corresponding response, for each client on server"""
    #Startup message to client. for getting input and breaking wail loop
    clientSock.send("Welcome to Tic Tac To".encode())

    #Handles massage from client to end. 
    while True:
        #recive commend from client
        cmd = clientSock.recv(4096).decode()
        ord = cmd.split(" ")

        #showing who played
        if cmd== "who":
            if len(players) > 0:
                playersList = ""
                for user in players:
                    playersList += str(user)
                    playersList += "\n"
                clientSock.send(playersList.encode())
            else:
                clientSock.send("There isn't any player".encode())

        #showing list of games
        elif cmd== "games":
            if len(games) > 0:
                GamesList = ""
                for game in games:
                    GamesList += str(game)
                    GamesList += "\n"
                clientSock.send(GamesList.encode())
            else:
                clientSock.send("There isn't any game".encode())      

        #Help list for input
        elif cmd == "help":
            clientSock.send(help_command.encode())
        
        elif cmd == "exit":
            print("Disconnecting ....")
            clientSock.send("DISC".encode())
            clientSock.close()
            print("Disconnected.")
            break

        #Handling cmd for doing :
        elif ord[0] =="login" and ord[1]:
            userN = ord[1]
            flag = False

            for user in players:
                #if user existed in palyers:
                if user.userN == userN:
                     current = user
                     flag = True
                     #send login message
                     print(current.userN + "Logged in")
            
            #if user dosen't exist in players
            if not flag:
                lock.acquire()
                #create new palyers to list of players 
                current = Player(userN,clientSock)
                players.append(current)
                print(current.userN + "created and logged in")
                lock.release()
            
            #send greeting message
                msg = current.userN + " wellcome and have FUN!"
            clientSock.send(msg.encode())

        #playing order:
        elif ord[0] == "play":
            #find for player an opponet
            current.setAval()
            opp = None
            while opp is None:
                for Gamer in players:
                    if Gamer.userN != current.userN and Gamer.state == "A":
                         opp = Gamer
                #sleep for adding opponent in game
                if opp == None:
                    time.sleep(10)
                
                #if a gamer founded as opp genarate UUID for this game and add it to Games:list
                else:
                    lock.acquire()
                    id = uuid.uuid4()
                    game = Board(opp, current, id)

                    #print new game created message
                    print("new Game board with id:" + str(id) + " is created.")
                    
                    games.append(game)
                    opp.Busy()
                    current.Busy()
                    lock.release()

                    # Starting game
                    start(game)

                    #when game is ended remove this game from Games:list and set gamers free.
                    lock.acquire()
                    games.remove(id)
                    current.login()
                    opp.login()
                    lock.release()
        else:
            clientSock.send("400 ERR".encode())

         
#main Loop 
while True:
    clientSock, addr = socket.accept()
    print("Connected to new client")
    _thread.start_new_thread(connect, (clientSock,))

socket.close()



        


          