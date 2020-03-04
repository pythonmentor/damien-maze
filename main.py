# -tc- pas de majuscules dans les noms de modules. L'usage de classe est
# -tc- est excellent
from RawLab import RawLab
from Hallways import Hallways
from Doorways import Doorways
from DisplayTerminal import display_terminal
from FinalMaze import FinalMaze


def main():
    # -tc- En anglais,  c'est width et length
    widht, lenght = (
        input("Enter an int as widht\n"),
        input("Enter an int as lenght\n"),
    )

    input_user = (
        0  # is_user_input_ok = True -tc- utilise True/False plutôt que 1/0
    )

    while not input_user:
        try:
            widht = int(widht)
            lenght = int(lenght)

            # -tc- Si tu veux que que width == length, pourquoi demander deux
            # -tc- valeurs? Demande simplement la dimension du labyrinthe.

            # -tc- Le raise ValueError n'est pas nécessaire. Réorganise ta
            # -tc- condition
            # -tc- if width == length:
            # -tc-     input_user = True
            if widht != lenght:
                raise ValueError
            else:
                input_user = 1
        except ValueError:
            # -tc- Your maze has to be a square. Width and length have to integers.
            print(
                "You're maze as to be square. Widht and lenght as to be integer"
            )
            # -tc- ou simpement
            # -tc- width = length = input("Enter the dimension as an int: ")
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

