class RawLab:
    """
	Create a raw maze, cells and inside walls only. No hallways. No enter. No exit.
	"""

    def __init__(self, widht, lenght):
        self.lenght = lenght
        self.widht = widht
        self.id_cells = self.create_id_cells(self.lenght, self.widht)
        self.h_walls = self.make_h_walls(self.lenght, self.widht)
        self.v_walls = self.make_v_walls(self.lenght, self.widht)

    def create_id_cells(self, widht, lenght):
        # Creating cells of a maze and assigning each one an id
        # Array of widht x lenght
        array = [[0 for l in range(lenght)] for w in range(widht)]
        cell_id = 1
        for i in range(len(array)):
            for j in range(len(array[0])):
                array[i][j] = cell_id
                cell_id += 1
        return array

    def make_h_walls(self, widht, lenght):
        # Creating inside horizontals walls ((widht-1) x lenght)
        array = [[1 for l in range(lenght)] for w in range(widht - 1)]

        return array

    def make_v_walls(self, widht, lenght):
        # Creating inside verticals walls (widht x (lenght-1))
        # 1 mean wall exist
        array = [[1 for l in range(lenght - 1)] for w in range(widht)]

        return array

