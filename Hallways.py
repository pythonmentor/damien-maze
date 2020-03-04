import random

class Hallways:
	'''
	Create hallways in a RawLab object, by getting rid of (lenght x widht)-1 walls, randomly choosen
	'''
	def __init__(self, widht, lenght, id_cells_rawlab_object, 
				h_walls_rawlab_object, v_walls_rawlab_object):
		
		self.widht = widht
		self.lenght = lenght
		self.id_cells = id_cells_rawlab_object
		self.h_walls = h_walls_rawlab_object
		self.v_walls = v_walls_rawlab_object

		self.walls_to_get_rid_off = (self.lenght * self.widht) - 1
		
	def making_hallways(self):
		wall = 0
		while wall <= self.walls_to_get_rid_off:
			#Choosing wall, getting is coordinnates and orientation
			w_i_w, w_i_l, choice = self.choosing_walls()
			if not choice%2: #If v_walls
				if self.id_cells[w_i_w][w_i_l] != self.id_cells[w_i_w][w_i_l+1]:
				#If id_cells !=, getting rid of the wall and merging there id
					self.get_rid_of_walls(w_i_w, w_i_l, choice)
					self.merging_id_cells(self.id_cells[w_i_w][w_i_l], self.id_cells[w_i_w][w_i_l+1])
				else:
				#Else, we don't wan't to get rid of this one
					if wall < self.walls_to_get_rid_off:
						continue
					else:
						break
			else: #If h_walls
				if self.id_cells[w_i_w][w_i_l] != self.id_cells[w_i_w+1][w_i_l]:
					self.get_rid_of_walls(w_i_w, w_i_l, choice)
					self.merging_id_cells(self.id_cells[w_i_w][w_i_l], self.id_cells[w_i_w+1][w_i_l])
				else:
					if wall < self.walls_to_get_rid_off:
						continue
					else:
						break
			wall += 1
					
		
	def choosing_walls(self):
	#Choosing randomly wich wall we want to getting rid
		choice = random.randrange(1, 100)
		#If even, a v_walls has been choosen
		if not choice%2:
			wall_in_widht = random.randrange(0, len(self.v_walls))
			wall_in_lenght = random.randrange(0, len(self.v_walls[0]))
		#If odd, well obviously it's an h_walls
		else:
			wall_in_widht = random.randrange(0, len(self.h_walls))
			wall_in_lenght = random.randrange(0, len(self.h_walls[0]))
			
		return wall_in_widht, wall_in_lenght, choice
		
	def get_rid_of_walls(self, wall_in_widht, wall_in_lenght, choice):
		if not choice%2:
			#0 mean there no wall here
			self.v_walls[wall_in_widht][wall_in_lenght] = 0
		else:
			self.h_walls[wall_in_widht][wall_in_lenght] = 0
			
	def merging_id_cells(self, first_cell_id, second_cell_id):
			#Counting each id
			count_first_cell = sum(self.id_cells[i].count(first_cell_id) for i in range(len(self.id_cells)))
			count_second_cell = sum(self.id_cells[i].count(second_cell_id) for i in range(len(self.id_cells)))
			
			#And merging id cells
			if count_first_cell == count_second_cell:
				for i in range(len(self.id_cells)):
					for j in range(len(self.id_cells[0])):
						if self.id_cells[i][j] == second_cell_id:
							self.id_cells[i][j] = first_cell_id

			elif count_first_cell > count_second_cell:
				for i in range(len(self.id_cells)):
					for j in range(len(self.id_cells[0])):
						if self.id_cells[i][j] == second_cell_id:
							self.id_cells[i][j] = first_cell_id
							
			else:
				for i in range(len(self.id_cells)):
					for j in range(len(self.id_cells[0])):
						if self.id_cells[i][j] == first_cell_id:
							self.id_cells[i][j] = second_cell_id
							


				