import random


class Doorways:
    """
	Create random enter and exit for your maze
	"""

    def __init__(self, widht, lenght):

        self.widht = widht
        self.lenght = lenght

    def create_enter_and_exit(
        self,
    ):  # To do : Enter and exit can't be on the same side!!!
        enter_colonne = 0
        enter_ligne = 0
        exit_colonne = 0
        exit_ligne = 0

        while (enter_colonne, enter_ligne) == (exit_colonne, exit_ligne):
            # We wan't enter and exit to be on outside walls, so coordinates has to be (0, x) or (x, 0) or (w, x) or (x, w)
            enter_colonne = random.randrange(0, self.lenght - 1)
            enter_ligne = (
                random.randrange(0, self.widht - 1)
                if (enter_colonne == 0 or enter_colonne == self.lenght - 1)
                else random.choice([0, self.widht - 1])
            )

            exit_colonne = random.randrange(0, self.lenght - 1)
            exit_ligne = (
                random.randrange(0, self.widht - 1)
                if (exit_colonne == 0 or exit_colonne == self.lenght - 1)
                else random.choice([0, self.widht - 1])
            )

        return (enter_ligne, enter_colonne), (exit_ligne, exit_colonne)

    # -tc- Le plus simple à mon avis et moins essai-erreur:
    def create_enter_and_exit_simple(self):
        positions = set()
        for i in range(self.width):
            positions |= {
                (0, i),
                (i, 0),
                (self.width - 1, i),
                (i, self.width - 1),
            }
        return random.sample(positions, 2)

