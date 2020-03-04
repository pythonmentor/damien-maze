class FinalMaze:
	'''
	Creating our final maze. Adding external walls, enter and exit to our hallways
	'''
	
	def __init__(self, widht, lenght, h_walls, v_walls, enter, exit_maze):
		self.widht = widht
		self.lenght = lenght
		self.h_walls = h_walls
		self.v_walls = v_walls
		self.enter = enter
		self.exit_maze = exit_maze
		
	def final_maze(self):
		self.add_south_walls()
		self.add_east_walls()
		
		final_maze = [[(self.h_walls[w][l], self.v_walls[w][l]) for l in range(self.lenght)] for w in range(self.widht)]
		
		final_maze.insert(0, self.add_north_walls())
		
		final_maze = self.add_west_walls(final_maze)
		
		return final_maze
		
	def add_south_walls(self):
		'''
		Adding south external south walls (1), except if there is a enter/exit (0)
		'''
		new_south_walls = list()
		
		for i in range(len(self.h_walls[0])):
			if all([((len(self.h_walls), i) != self.enter), ((len(self.h_walls), i) != self.exit_maze)]):
			#If there is no doorways here...
				new_south_walls.append(1)
				#Creating a wall
			else:
			#Else, remaining empty, which is our enter/exit
				new_south_walls.append(0)
		
		self.h_walls.append(new_south_walls)

	def add_east_walls(self):
		'''
		Adding east external south walls (1), except if there is a enter/exit (0)
		'''
		v_walls_copy = self.v_walls
		
		for i in range(len(self.v_walls)):
			if all([((i, len(self.v_walls[i])) != self.enter), ((i, len(self.v_walls[i])) != self.exit_maze)]):
				v_walls_copy[i].append(1)
			else:
				v_walls_copy[i].append(0)
		
		self.v_walls = v_walls_copy
				
	def add_north_walls(self):
		'''
		Adding north external south walls (1), except if there is a enter/exit (0)
		'''
		north_walls = list()
		
		for l in range(len(self.h_walls[0])-1):
			if all([((0, l) != self.enter), ((0, l) != self.exit_maze)]):
				north_walls.append(1)
			else:
				north_walls.append(0)
				
		return north_walls
		
	def add_west_walls(self, maze):
		'''
		Adding west external south walls (1), except if there is a enter/exit (0)
		'''
		for w in range(len(maze)):
			if all([((w, 0) != self.enter), ((w, 0) != self.exit_maze)]):
				maze[w].insert(0, 1)
			else:
				maze[w].insert(0, 0)
				
		return maze

		
