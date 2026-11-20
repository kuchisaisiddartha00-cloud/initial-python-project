ASCII 3D Maze Runner Game
A simple, interactive maze navigation game written in Python. The player explores a predefined maze using keyboard commands. The game displays a first-person, 3D-style view in the terminal by using ASCII characters and a basic ray-casting technique.
Project Overview
The goal is to navigate through the maze without walking through walls and reach the exit. The player can rotate, move forward or backward, and display the complete maze from a top-down view.
Features
- First-person ASCII 3D-style maze display in the terminal.
- Keyboard-based player controls.
- Ray casting to estimate the distance from the player to walls.
- Wall collision checking to prevent movement through walls.
- Top-down maze display using the MAP command.
- Exit detection and a completion message when the player reaches the exit.
- Uses Python's built-in modules; no third-party packages are required.
Technologies Used
- Language: Python 3
- Editor: Visual Studio Code (or any Python IDE)
- Interface: Command-line terminal
- Python modules: math (the program also imports os, though it is not needed by the current game logic)
Requirements
- Python 3 installed on your computer.
- Visual Studio Code is recommended, but not required.
- No external Python libraries are required.
How to Run
1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Open the integrated terminal (Terminal → New Terminal).
4. Run the program:
   python ascii_3d_maze_runner.py
   On some Windows installations, use:
   py ascii_3d_maze_runner.py
5. Enter one command at a time when the game asks for input.
Game Controls
Key / Command	Action
W	Move forward in the direction the player is facing
S	Move backward
A	Turn left by 22.5 degrees
D	Turn right by 22.5 degrees
MAP	Display the maze from a top-down view
Q	Quit the game


The game reads one command at a time. Press Enter after typing a command.
How It Works
1. Maze setup: The maze is stored as a Python list of strings. The # character represents a wall and . represents an open path.
2. Player setup: The player's position is stored as X and Y coordinates, while the viewing direction is stored as an angle.
3. Ray casting: The program casts rays across the player's field of view. Each ray advances until it reaches a wall or the maximum viewing distance.
4. View rendering: The distance to each wall is used to calculate the height of the wall column. ASCII symbols are printed to create a first-person, 3D-style effect.
5. Movement and collision: The game calculates the proposed position for forward or backward movement. The is_wall() function checks the destination before the player's coordinates are updated.
6. Exit checking: The is_exit() function checks whether the player is at the exit coordinate. If so, the game displays a completion message and ends.
Main Functions
Function	Purpose
is_wall(x, y)	Checks whether a coordinate is outside the maze or contains a wall.
is_exit(x, y)	Checks whether the player has reached the exit coordinate.
cast_ray(angle)	Finds the distance to the nearest wall along a ray.
render_view()	Draws the first-person ASCII 3D-style view.
show_map()	Displays the full maze and the player's position.
main()	Runs the game loop, reads commands, and manages movement.


Project Structure
ASCII-3D-Maze-Runner/
├── ascii_3d_maze_runner.py
└── README.md
Current Scope and Possible Improvements
This is a small terminal-based demonstration. It uses one predefined maze and an ASCII 3D-style display; it is not a full 3D graphics game.

Possible future improvements include:
- Add multiple maze levels or randomly generated mazes.
- Add a timer, score, and move counter.
- Add difficulty settings.
- Create a graphical user interface.
- Add an automatic path-finding feature.
- Author
- NAME : KUCHI SAI SIDDARTHA
- CSE GEN AI IBM A
