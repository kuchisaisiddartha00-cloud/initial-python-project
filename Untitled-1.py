"""
ASCII 3D Maze Runner
VS Code compatible Python version.

Controls:
  W - Move forward
  S - Move backward
  A - Turn left
  D - Turn right
  Q - Quit

Run this file in the VS Code integrated terminal.
No external libraries are required.
"""

import math
import os

# # = wall, . = open path, E = exit
MAZE = [
    "###############",
    "#.....#.......#",
    "#.###.#.#####.#",
    "#...#...#.....#",
    "###.#####.###.#",
    "#...#.....#...#",
    "#.###.###.#.###",
    "#.....#...#...#",
    "#.#####.#####.#",
    "#.............#",
    "###############",
]

# Player starts in an open cell.
player_x = 1.5
player_y = 1.5
player_angle = 0.0  # 0 = east, pi/2 = south

SCREEN_WIDTH = 61
SCREEN_HEIGHT = 21
FOV = math.pi / 3
MAX_DEPTH = 16
ROTATION_STEP = math.pi / 8
MOVE_STEP = 0.35


def is_wall(x, y):
    """Return True if a position is outside the maze or inside a wall."""
    map_x = int(x)
    map_y = int(y)

    if map_y < 0 or map_y >= len(MAZE):
        return True
    if map_x < 0 or map_x >= len(MAZE[0]):
        return True

    return MAZE[map_y][map_x] == "#"


def is_exit(x, y):
    """Check whether the player has reached the exit cell."""
    return int(x) == len(MAZE[0]) - 2 and int(y) == len(MAZE) - 2


def cast_ray(angle):
    """Find the distance from the player to the nearest wall in one direction."""
    distance = 0.0
    step_size = 0.04

    while distance < MAX_DEPTH:
        distance += step_size
        test_x = player_x + math.cos(angle) * distance
        test_y = player_y + math.sin(angle) * distance

        if is_wall(test_x, test_y):
            return distance

    return MAX_DEPTH


def render_view():
    """Draw a simple first-person, ASCII 3D-style view of the maze."""
    screen = [[" " for _ in range(SCREEN_WIDTH)]
              for _ in range(SCREEN_HEIGHT)]

    for column in range(SCREEN_WIDTH):
        ray_angle = (
            player_angle - FOV / 2
            + (column / SCREEN_WIDTH) * FOV
        )

        distance = cast_ray(ray_angle)

        # Correct the fish-eye effect.
        corrected_distance = distance * math.cos(ray_angle - player_angle)
        corrected_distance = max(corrected_distance, 0.1)

        wall_height = int(SCREEN_HEIGHT / corrected_distance)
        wall_height = min(wall_height, SCREEN_HEIGHT)

        ceiling = (SCREEN_HEIGHT - wall_height) // 2
        floor = ceiling + wall_height

        # Choose a wall character based on distance.
        if distance < 2:
            wall_char = "#"
        elif distance < 4:
            wall_char = "X"
        elif distance < 7:
            wall_char = "+"
        elif distance < 11:
            wall_char = "."
        else:
            wall_char = " "

        for row in range(ceiling, min(floor, SCREEN_HEIGHT)):
            screen[row][column] = wall_char

        # Draw a simple floor texture.
        for row in range(floor, SCREEN_HEIGHT):
            if row > SCREEN_HEIGHT * 0.75:
                screen[row][column] = "_"
            else:
                screen[row][column] = "."

    print("\n" + "=" * SCREEN_WIDTH)
    print(" " * 20 + "ASCII 3D MAZE RUNNER")
    print("=" * SCREEN_WIDTH)

    for row in screen:
        print("".join(row))

    direction_names = ["EAST", "SOUTH", "WEST", "NORTH"]
    direction_index = int(
        ((player_angle % (2 * math.pi)) + math.pi / 4)
        / (math.pi / 2)
    ) % 4

    print("-" * SCREEN_WIDTH)
    print(f"Direction: {direction_names[direction_index]}")
    print("Controls: W = forward | S = backward | A = left | D = right | Q = quit")


def show_map():
    """Show the top-down maze and the player's current position."""
    print("\nMap:")
    for y, row in enumerate(MAZE):
        line = ""
        for x, cell in enumerate(row):
            if int(player_x) == x and int(player_y) == y:
                line += "P"
            elif x == len(row) - 2 and y == len(MAZE) - 2:
                line += "E"
            else:
                line += cell
        print(line)


def main():
    global player_x, player_y, player_angle

    print("Welcome to ASCII 3D Maze Runner!")
    print("Find the exit. Enter one command at a time.")
    print("Tip: Type MAP to see the maze from above.")

    while True:
        render_view()
        command = input("\nEnter move (W/A/S/D, MAP, Q): ").strip().upper()

        if command == "Q":
            print("Thanks for playing!")
            break

        if command == "MAP":
            show_map()
            continue

        if command == "A":
            player_angle -= ROTATION_STEP
        elif command == "D":
            player_angle += ROTATION_STEP
        elif command in ("W", "S"):
            direction = 1 if command == "W" else -1
            new_x = player_x + math.cos(player_angle) * MOVE_STEP * direction
            new_y = player_y + math.sin(player_angle) * MOVE_STEP * direction

            # Check the destination before moving, so the player cannot pass through walls.
            if not is_wall(new_x, new_y):
                player_x = new_x
                player_y = new_y
            else:
                print("A wall is blocking the way!")
        else:
            print("Invalid command. Use W, A, S, D, MAP, or Q.")

        if is_exit(player_x, player_y):
            render_view()
            print("\nCongratulations! You reached the exit and completed the maze!")
            break


if __name__ == "__main__":
    main()