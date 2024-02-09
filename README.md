## Tic Tac Toe: A Python Multiplayer Game

**Welcome to Tic Tac Toe!** This project brings the classic pencil-and-paper game to life as a fun and interactive multiplayer experience in Python. It features:

* **Multiple players:** Connect to the server and challenge friends or compete against random opponents.
* **Matching system:** The server automatically finds you a suitable opponent based on your availability and skill level.
* **Text-based interface:** A simple and familiar text-based interface makes gameplay easy and intuitive.
* **Chat commands:** Use commands like `who`, `games`, `login`, `play`, `place`, and `exit` to manage your account, view ongoing games, and make moves.
* **Robust game logic:** Enjoy fair and accurate gameplay thanks to well-structured Python code that handles board management, move validation, and game states.

### How to play:

1. **Clone or download this repository.**
2. **Install the required libraries:**

```bash
pip install socket uuid threading
```

3. "Run the server script:"
   
```bash
python server.py
```
4. Open multiple terminal windows and run the client script in each window:
```bash
python client.py
```

5. **Once connected to the server, use the following commands:**

| Command | Description |
|---|---|
| `who` | Shows a list of online players. |
| `games` | Shows a list of ongoing games. |
| `login <username>` | Logs in with a username. |
| `help` | Shows a list of available commands. |
| `play` | Finds an opponent and starts a new game. |
| `place <position>` | Makes a move in the current game (position: 1-9). |
| `exit` | Disconnects from the server. |

### Code structure:

The code is divided into four main Python files:

* **`board.py`:** Defines the game board logic, including board representation, move validation, and win conditions.
* **`player.py`:** Manages player information, connections, and login/logout functionality.
* **`server.py`:** Implements the server-side logic, handling player connections, matchmaking, game creation, message routing, and command processing.
* **`client.py`:** Implements the client-side logic, connecting to the server, sending commands, receiving updates, and displaying the game interface.

### Contributing:

We welcome contributions to this project! Feel free to fork the repository, make improvements, and submit pull requests.

### License:

This project is licensed under the MIT License. See the LICENSE file for more details.

### Additional notes:

* You can customize the game board size and winning conditions in the `board.py` file.
* You can add more chat commands and features to the game.
* Feel free to explore the code, experiment with different aspects of the game, and let us know your feedback!

I hope this README.md provides a comprehensive and informative overview of your Tic Tac Toe project!
