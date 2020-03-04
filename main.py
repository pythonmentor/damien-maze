# -tc- pas de majuscules dans les noms de modules. L'usage de classe est
# -tc- est excellent
from RawLab import RawLab
from Hallways import Hallways
from Doorways import Doorways
from DisplayTerminal import display_terminal
from FinalMaze import FinalMaze


def main():

    widht, lenght = (
        input("Enter an int as widht\n"),
        input("Enter an int as lenght\n"),
    )

    input_user = 0

    while not input_user:
        try:
            widht = int(widht)
            lenght = int(lenght)

            if widht != lenght:
                raise ValueError
            else:
                input_user = 1
        except ValueError:
            print(
                "You're maze as to be square. Widht and lenght as to be integer"
            )
            widht, lenght = (
                input("Enter an int as widht:\n"),
                input("Enter an int as lenght:\n"),
            )

    maze = RawLab(widht, lenght)

    hallways = Hallways(
        maze.widht, maze.lenght, maze.id_cells, maze.h_walls, maze.v_walls
    )
    hallways.making_hallways()

    doorways = Doorways(maze.widht, maze.lenght)
    enter, exit_maze = doorways.create_enter_and_exit()

    final_maze = FinalMaze(
        maze.widht,
        maze.lenght,
        hallways.h_walls,
        hallways.v_walls,
        enter,
        exit_maze,
    )

    display_terminal(final_maze.final_maze())


# -tc- L'usage de cette fonction est recommandé pour pouvoir éventuellement
# -tc- importer main() dans un autre module
if __name__ == "__main__":
    main()

