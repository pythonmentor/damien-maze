def display_terminal(final_maze):

	for w in range(len(final_maze)):
		for l in range(len(final_maze[w])):
		
			if isinstance(final_maze[w][l], int):
				if final_maze[w][l] and w: #If there is a wall and a west one...
					print('|', end='')
					
				elif final_maze[w][l] and not w: #... Or a north one
					if (w, l) == (0, 0): #If we are a top-left corner
						print(' ', end='')
						
					print(f'_ ', end='')
				
				else:
					print(' ', end='')
			
			elif isinstance(final_maze[w][l], tuple):
				if final_maze[w][l][0]:
					print('_', end='')
				else:
					print(' ', end='')
				
				if final_maze[w][l][1]:
					print('|', end='')
				else:
					print(' ', end='')
				
		print()